from dataclasses import dataclass
import json

import cv2, io, numpy as np
from PIL import Image
from enum import IntEnum

from base64 import b64decode


@dataclass
class ImageLabelFile:
    name:str
    searchMethod: int
    ImgBase64: str
    RangeX: int
    RangeY: int
    RangeWidth: int
    RangeHeight: int
    TargetX: int
    TargetY: int
    TargetWidth: int
    TargetHeight: int
    matchDegree: float
    
    @staticmethod
    def from_json(json_str):
        return ImageLabelFile(**json.loads(json_str))

    @staticmethod
    def from_file(filepath):
        with open(filepath, 'r', encoding='utf8') as file:
            d = json.load(file)
        return ImageLabelFile(**d)

class SearchMethod(IntEnum):
    
    # "平方差匹配"
    SqDiff = 0
    # "标准差匹配"
    SqDiffNormed = 1
    # "相关匹配"
    CCorr = 2
    # "标准相关匹配"
    CCorrNormed = 3
    # "相关系数匹配"
    CCoeff = 4
    # "标准相关系数匹配"
    CCoeffNormed = 5
    # "严格匹配"
    StrictMatch = 6
    # "随机严格匹配"
    StrictMatchRND = 7
    # "透明度匹配"
    OpacityDiff = 8
    # "相似匹配"
    SimilarMatch = 9

def PIL2cv2(img:Image.Image)->cv2.Mat:
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)

class ImageLabel:
    
    AVAILABLE_METHODS = {
        SearchMethod.SqDiffNormed: cv2.TM_SQDIFF_NORMED,
        SearchMethod.CCorrNormed: cv2.TM_CCORR_NORMED,
        SearchMethod.CCoeffNormed: cv2.TM_CCOEFF_NORMED
    }
    
    def __init__(self, ImageLableFile:ImageLabelFile):
        self.name = ImageLableFile.name
        self.searchMethod = ImageLableFile.searchMethod
        self.Img = PIL2cv2(Image.open(io.BytesIO(b64decode(ImageLableFile.ImgBase64))))
        self.RangeX = ImageLableFile.RangeXfr
        self.RangeY = ImageLableFile.RangeY
        self.RangeWidth = ImageLableFile.RangeWidth
        self.RangeHeight = ImageLableFile.RangeHeight
        self.TargetX = ImageLableFile.TargetX
        self.TargetY = ImageLableFile.TargetY
        self.TargetWidth = ImageLableFile.TargetWidth
        self.TargetHeight = ImageLableFile.TargetHeight
        self.matchDegree = ImageLableFile.matchDegree
        

    @staticmethod
    def from_file(path):
        return ImageLabel(ImageLabelFile.from_file(path))


    def search(self, frame:cv2.Mat) -> tuple[float, cv2.typing.Point]: #match degree, match loc
        small = self.Img
        big = frame[self.RangeY:self.RangeY + self.RangeHeight, self.RangeX:self.RangeX + self.RangeWidth]
        result = None
        
        matchDegree = 0
        
        result = cv2.matchTemplate(big, small, method=self.AVAILABLE_METHODS[self.searchMethod])
        min_, max_, minLoc, maxLoc = cv2.minMaxLoc(result)
        
        result_location = None
        if self.searchMethod == SearchMethod.SqDiffNormed:
            
            matchDegree = 1 - min_
            result_location = minLoc
        elif self.searchMethod == SearchMethod.CCorrNormed:
            matchDegree = max_
            result_location = maxLoc
        elif self.searchMethod == SearchMethod.CCoeffNormed:
            matchDegree = (max_ + 1) / 2
            result_location = maxLoc
        else:
            raise NotImplementedError("Method not implemented")
        
        result_location = (result_location[0] + self.RangeX, result_location[1] + self.RangeY)
        return matchDegree, result_location
        
