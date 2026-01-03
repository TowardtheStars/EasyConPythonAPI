# Generated from EasyScript.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .EasyScriptParser import EasyScriptParser
else:
    from EasyScriptParser import EasyScriptParser

# This class defines a complete listener for a parse tree produced by EasyScriptParser.
class EasyScriptListener(ParseTreeListener):

    # Enter a parse tree produced by EasyScriptParser#program.
    def enterProgram(self, ctx:EasyScriptParser.ProgramContext):
        pass

    # Exit a parse tree produced by EasyScriptParser#program.
    def exitProgram(self, ctx:EasyScriptParser.ProgramContext):
        pass


    # Enter a parse tree produced by EasyScriptParser#statement.
    def enterStatement(self, ctx:EasyScriptParser.StatementContext):
        pass

    # Exit a parse tree produced by EasyScriptParser#statement.
    def exitStatement(self, ctx:EasyScriptParser.StatementContext):
        pass


    # Enter a parse tree produced by EasyScriptParser#expression.
    def enterExpression(self, ctx:EasyScriptParser.ExpressionContext):
        pass

    # Exit a parse tree produced by EasyScriptParser#expression.
    def exitExpression(self, ctx:EasyScriptParser.ExpressionContext):
        pass


    # Enter a parse tree produced by EasyScriptParser#comment.
    def enterComment(self, ctx:EasyScriptParser.CommentContext):
        pass

    # Exit a parse tree produced by EasyScriptParser#comment.
    def exitComment(self, ctx:EasyScriptParser.CommentContext):
        pass


    # Enter a parse tree produced by EasyScriptParser#print_statement.
    def enterPrint_statement(self, ctx:EasyScriptParser.Print_statementContext):
        pass

    # Exit a parse tree produced by EasyScriptParser#print_statement.
    def exitPrint_statement(self, ctx:EasyScriptParser.Print_statementContext):
        pass


    # Enter a parse tree produced by EasyScriptParser#alert_statement.
    def enterAlert_statement(self, ctx:EasyScriptParser.Alert_statementContext):
        pass

    # Exit a parse tree produced by EasyScriptParser#alert_statement.
    def exitAlert_statement(self, ctx:EasyScriptParser.Alert_statementContext):
        pass


    # Enter a parse tree produced by EasyScriptParser#key_statement.
    def enterKey_statement(self, ctx:EasyScriptParser.Key_statementContext):
        pass

    # Exit a parse tree produced by EasyScriptParser#key_statement.
    def exitKey_statement(self, ctx:EasyScriptParser.Key_statementContext):
        pass


    # Enter a parse tree produced by EasyScriptParser#stick_statement.
    def enterStick_statement(self, ctx:EasyScriptParser.Stick_statementContext):
        pass

    # Exit a parse tree produced by EasyScriptParser#stick_statement.
    def exitStick_statement(self, ctx:EasyScriptParser.Stick_statementContext):
        pass


    # Enter a parse tree produced by EasyScriptParser#wait_statement.
    def enterWait_statement(self, ctx:EasyScriptParser.Wait_statementContext):
        pass

    # Exit a parse tree produced by EasyScriptParser#wait_statement.
    def exitWait_statement(self, ctx:EasyScriptParser.Wait_statementContext):
        pass


    # Enter a parse tree produced by EasyScriptParser#for_statement.
    def enterFor_statement(self, ctx:EasyScriptParser.For_statementContext):
        pass

    # Exit a parse tree produced by EasyScriptParser#for_statement.
    def exitFor_statement(self, ctx:EasyScriptParser.For_statementContext):
        pass


    # Enter a parse tree produced by EasyScriptParser#break_statement.
    def enterBreak_statement(self, ctx:EasyScriptParser.Break_statementContext):
        pass

    # Exit a parse tree produced by EasyScriptParser#break_statement.
    def exitBreak_statement(self, ctx:EasyScriptParser.Break_statementContext):
        pass


    # Enter a parse tree produced by EasyScriptParser#continue_statement.
    def enterContinue_statement(self, ctx:EasyScriptParser.Continue_statementContext):
        pass

    # Exit a parse tree produced by EasyScriptParser#continue_statement.
    def exitContinue_statement(self, ctx:EasyScriptParser.Continue_statementContext):
        pass


    # Enter a parse tree produced by EasyScriptParser#assignment.
    def enterAssignment(self, ctx:EasyScriptParser.AssignmentContext):
        pass

    # Exit a parse tree produced by EasyScriptParser#assignment.
    def exitAssignment(self, ctx:EasyScriptParser.AssignmentContext):
        pass


    # Enter a parse tree produced by EasyScriptParser#function_definition.
    def enterFunction_definition(self, ctx:EasyScriptParser.Function_definitionContext):
        pass

    # Exit a parse tree produced by EasyScriptParser#function_definition.
    def exitFunction_definition(self, ctx:EasyScriptParser.Function_definitionContext):
        pass


    # Enter a parse tree produced by EasyScriptParser#function_call.
    def enterFunction_call(self, ctx:EasyScriptParser.Function_callContext):
        pass

    # Exit a parse tree produced by EasyScriptParser#function_call.
    def exitFunction_call(self, ctx:EasyScriptParser.Function_callContext):
        pass


    # Enter a parse tree produced by EasyScriptParser#complex_assignment.
    def enterComplex_assignment(self, ctx:EasyScriptParser.Complex_assignmentContext):
        pass

    # Exit a parse tree produced by EasyScriptParser#complex_assignment.
    def exitComplex_assignment(self, ctx:EasyScriptParser.Complex_assignmentContext):
        pass


    # Enter a parse tree produced by EasyScriptParser#if_statement.
    def enterIf_statement(self, ctx:EasyScriptParser.If_statementContext):
        pass

    # Exit a parse tree produced by EasyScriptParser#if_statement.
    def exitIf_statement(self, ctx:EasyScriptParser.If_statementContext):
        pass


    # Enter a parse tree produced by EasyScriptParser#return_statement.
    def enterReturn_statement(self, ctx:EasyScriptParser.Return_statementContext):
        pass

    # Exit a parse tree produced by EasyScriptParser#return_statement.
    def exitReturn_statement(self, ctx:EasyScriptParser.Return_statementContext):
        pass


    # Enter a parse tree produced by EasyScriptParser#tool_statement.
    def enterTool_statement(self, ctx:EasyScriptParser.Tool_statementContext):
        pass

    # Exit a parse tree produced by EasyScriptParser#tool_statement.
    def exitTool_statement(self, ctx:EasyScriptParser.Tool_statementContext):
        pass


    # Enter a parse tree produced by EasyScriptParser#amiibo_statement.
    def enterAmiibo_statement(self, ctx:EasyScriptParser.Amiibo_statementContext):
        pass

    # Exit a parse tree produced by EasyScriptParser#amiibo_statement.
    def exitAmiibo_statement(self, ctx:EasyScriptParser.Amiibo_statementContext):
        pass



del EasyScriptParser