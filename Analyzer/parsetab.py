
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftIGUALESDISTINTOSleftMAYORIGUALMENORIGUALMAYORMENORleftMASMENOSleftMULTDIVMODrightPOTrightNOTrightUMINUSleftPARIZQPARDERLLAVIZQLLAVDERAND BOOL CHAR CHARID COMA CORDER CORIZQ COS DISTINTOS DIV DOSPUNTOS ELSE ELSEIF END FALSE FLOAT FLOAT64 FLOATID FUNCTION GLOBAL ID IF IGUAL IGUALES INT64 INTID LLAVDER LLAVIZQ LOCAL LOG LOG10 LOWERCASE MAS MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS MOD MULT NOT NULO OR PARDER PARIZQ PARSE POT PRINT PRINTLN PUNTO PUNTOCOMA SIN SQRT STRING STRINGID TAN TRUE TRUNC TYPEOF UPPERCASEinicio : instruccionesglbinstruccionesglb : instruccionesglb instruccionglb\n                        | instruccionglbinstruccionglb  : funcionINS PUNTOCOMA\n                       | declaracionglb PUNTOCOMA\n                       | printINS PUNTOCOMA\n                       | llamadaFunc PUNTOCOMAdeclaracionglb : ID\n                      | ID IGUAL expresion\n                      | ID IGUAL expresion DOSPUNTOS DOSPUNTOS tiposfuncionINS : FUNCTION ID PARIZQ PARDER sentencia END\n                  | FUNCTION ID PARIZQ params PARDER sentencia ENDparams : params COMA ID\n              | IDllamadaFunc : ID PARIZQ PARDER\n                   | ID PARIZQ listParams PARDERlistParams :  listParams COMA expresion\n                  | expresioninstrucciones : instrucciones instruccion\n                    | instruccioninstruccion  : printINS PUNTOCOMA\n                    | ifINS PUNTOCOMA\n                    | declaracionINS PUNTOCOMA\n                    | llamadaFunc PUNTOCOMAsentencia : instruccionesprintINS  : PRINTLN PARIZQ expresion PARDERprintINS  : PRINT PARIZQ expresion PARDERdeclaracionINS : ID\n                      | ID IGUAL expresion\n                      | ID IGUAL expresion DOSPUNTOS DOSPUNTOS tipos\n                      | accesos ID\n                      | accesos ID IGUAL expresion\n                      | accesos ID IGUAL expresion DOSPUNTOS DOSPUNTOS tipostipos : INT64\n             | FLOAT64\n             | STRING\n             | BOOL\n             | CHARaccesos : LOCAL\n               | GLOBALifINS : IF expresion sentencia END\n             | IF expresion sentencia ELSE sentencia END\n             | IF expresion sentencia elseIfLista ENDelseIfLista   : ELSEIF expresion sentencia\n                     | ELSEIF expresion sentencia ELSE sentencia\n                     | ELSEIF expresion sentencia elseIfListaexpresion    : MENOS expresion %prec UMINUS\n                    | NOT expresion %prec UMINUS\n\n                    | expresion MAS expresion\n                    | expresion MENOS expresion\n                    | expresion MULT expresion\n                    | expresion DIV expresion\n                    | expresion MOD expresion\n                    | expresion POT expresion\n\n                    | expresion MAYOR expresion\n                    | expresion MENOR expresion\n                    | expresion MAYORIGUAL expresion\n                    | expresion MENORIGUAL expresion\n                    | expresion IGUALES expresion\n                    | expresion DISTINTOS expresion\n\n                    | expresion OR expresion\n                    | expresion AND expresion\n                    | expValorexpValor : PARIZQ expresion PARDER\n                | INTID\n                | FLOATID\n                | STRINGID\n                | expCHAR\n                | expNativas\n                | TRUE\n                | FALSE\n                | IDexpCHAR : CHARIDexpNativas : LOG10 PARIZQ expresion PARDER\n                  | LOG PARIZQ expresion COMA expresion PARDER\n                  | SIN PARIZQ expresion PARDER\n                  | COS PARIZQ expresion PARDER\n                  | TAN PARIZQ expresion PARDER\n                  | SQRT PARIZQ expresion PARDER\n                  | UPPERCASE PARIZQ expresion PARDER\n                  | LOWERCASE PARIZQ expresion PARDER\n                  | PARSE PARIZQ INT64 COMA expresion PARDER\n                  | PARSE PARIZQ FLOAT64 COMA expresion PARDER\n                  | TRUNC PARIZQ INT64 COMA expresion PARDER\n                  | FLOAT PARIZQ expresion PARDER\n                  | STRING PARIZQ expresion PARDER\n                  | TYPEOF PARIZQ expresion PARDER'
    
_lr_action_items = {'FUNCTION':([0,2,3,12,13,14,15,16,],[8,8,-3,-2,-4,-5,-6,-7,]),'ID':([0,2,3,8,12,13,14,15,16,18,19,20,21,22,23,25,26,27,28,29,30,31,32,33,34,35,36,56,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,76,77,78,79,80,81,82,83,86,87,88,90,95,96,101,102,103,104,105,106,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,138,140,141,142,143,144,145,155,156,157,158,159,160,161,162,163,164,165,166,167,168,171,179,181,183,184,185,186,190,196,],[9,9,-3,17,-2,-4,-5,-6,-7,23,23,23,23,55,-72,23,23,-63,23,-65,-66,-67,-68,-69,-70,-71,-73,93,23,23,23,23,23,23,23,23,23,23,23,23,23,23,-47,-48,23,23,23,23,23,23,23,23,23,23,23,23,93,-20,23,146,-39,-40,93,148,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,23,-19,-21,-22,-23,-24,93,-74,23,-76,-77,-78,-79,-80,-81,23,23,23,-85,-86,-87,23,93,23,-75,-82,-83,-84,93,93,]),'PRINTLN':([0,2,3,12,13,14,15,16,23,27,29,30,31,32,33,34,35,36,56,73,74,95,96,105,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,140,141,142,143,144,145,155,157,158,159,160,161,162,166,167,168,179,183,184,185,186,190,196,],[10,10,-3,-2,-4,-5,-6,-7,-72,-63,-65,-66,-67,-68,-69,-70,-71,-73,10,-47,-48,10,-20,10,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,-19,-21,-22,-23,-24,10,-74,-76,-77,-78,-79,-80,-81,-85,-86,-87,10,-75,-82,-83,-84,10,10,]),'PRINT':([0,2,3,12,13,14,15,16,23,27,29,30,31,32,33,34,35,36,56,73,74,95,96,105,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,140,141,142,143,144,145,155,157,158,159,160,161,162,166,167,168,179,183,184,185,186,190,196,],[11,11,-3,-2,-4,-5,-6,-7,-72,-63,-65,-66,-67,-68,-69,-70,-71,-73,11,-47,-48,11,-20,11,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,-19,-21,-22,-23,-24,11,-74,-76,-77,-78,-79,-80,-81,-85,-86,-87,11,-75,-82,-83,-84,11,11,]),'$end':([1,2,3,12,13,14,15,16,],[0,-1,-3,-2,-4,-5,-6,-7,]),'PUNTOCOMA':([4,5,6,7,9,23,24,27,29,30,31,32,33,34,35,36,50,73,74,89,91,92,93,97,98,99,100,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,139,146,149,150,151,152,153,154,155,157,158,159,160,161,162,166,167,168,169,172,178,182,183,184,185,186,189,192,193,198,],[13,14,15,16,-8,-72,-9,-63,-65,-66,-67,-68,-69,-70,-71,-73,-15,-47,-48,-16,-26,-27,-28,141,142,143,144,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,-11,-31,-10,-34,-35,-36,-37,-38,-74,-76,-77,-78,-79,-80,-81,-85,-86,-87,-29,-12,-41,-32,-75,-82,-83,-84,-43,-30,-42,-33,]),'IGUAL':([9,93,146,],[18,138,171,]),'PARIZQ':([9,10,11,17,18,19,20,21,25,26,28,37,38,39,40,41,42,43,44,45,46,47,48,49,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,77,78,79,80,81,82,83,86,87,88,90,93,101,138,156,163,164,165,171,181,],[19,20,21,22,28,28,28,28,28,28,28,76,77,78,79,80,81,82,83,84,85,86,87,88,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,19,28,28,28,28,28,28,28,28,]),'MENOS':([18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,52,53,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,86,87,88,90,101,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,134,135,136,137,138,145,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,171,173,174,175,176,181,182,183,184,185,186,190,],[25,25,25,25,-72,60,25,25,-63,25,-65,-66,-67,-68,-69,-70,-71,-73,60,60,60,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-47,-48,60,25,25,25,25,25,25,25,25,25,25,25,25,25,-49,-50,-51,-52,-53,-54,60,60,60,60,60,60,60,60,-64,60,60,60,60,60,60,60,60,60,60,60,60,25,60,-74,25,-76,-77,-78,-79,-80,-81,25,25,25,-85,-86,-87,60,25,60,60,60,60,25,60,-75,-82,-83,-84,60,]),'NOT':([18,19,20,21,25,26,28,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,77,78,79,80,81,82,83,86,87,88,90,101,138,156,163,164,165,171,181,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'INTID':([18,19,20,21,25,26,28,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,77,78,79,80,81,82,83,86,87,88,90,101,138,156,163,164,165,171,181,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'FLOATID':([18,19,20,21,25,26,28,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,77,78,79,80,81,82,83,86,87,88,90,101,138,156,163,164,165,171,181,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'STRINGID':([18,19,20,21,25,26,28,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,77,78,79,80,81,82,83,86,87,88,90,101,138,156,163,164,165,171,181,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'TRUE':([18,19,20,21,25,26,28,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,77,78,79,80,81,82,83,86,87,88,90,101,138,156,163,164,165,171,181,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'FALSE':([18,19,20,21,25,26,28,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,77,78,79,80,81,82,83,86,87,88,90,101,138,156,163,164,165,171,181,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'CHARID':([18,19,20,21,25,26,28,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,77,78,79,80,81,82,83,86,87,88,90,101,138,156,163,164,165,171,181,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'LOG10':([18,19,20,21,25,26,28,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,77,78,79,80,81,82,83,86,87,88,90,101,138,156,163,164,165,171,181,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'LOG':([18,19,20,21,25,26,28,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,77,78,79,80,81,82,83,86,87,88,90,101,138,156,163,164,165,171,181,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'SIN':([18,19,20,21,25,26,28,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,77,78,79,80,81,82,83,86,87,88,90,101,138,156,163,164,165,171,181,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'COS':([18,19,20,21,25,26,28,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,77,78,79,80,81,82,83,86,87,88,90,101,138,156,163,164,165,171,181,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'TAN':([18,19,20,21,25,26,28,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,77,78,79,80,81,82,83,86,87,88,90,101,138,156,163,164,165,171,181,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'SQRT':([18,19,20,21,25,26,28,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,77,78,79,80,81,82,83,86,87,88,90,101,138,156,163,164,165,171,181,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'UPPERCASE':([18,19,20,21,25,26,28,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,77,78,79,80,81,82,83,86,87,88,90,101,138,156,163,164,165,171,181,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'LOWERCASE':([18,19,20,21,25,26,28,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,77,78,79,80,81,82,83,86,87,88,90,101,138,156,163,164,165,171,181,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'PARSE':([18,19,20,21,25,26,28,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,77,78,79,80,81,82,83,86,87,88,90,101,138,156,163,164,165,171,181,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'TRUNC':([18,19,20,21,25,26,28,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,77,78,79,80,81,82,83,86,87,88,90,101,138,156,163,164,165,171,181,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'FLOAT':([18,19,20,21,25,26,28,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,77,78,79,80,81,82,83,86,87,88,90,101,138,156,163,164,165,171,181,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'STRING':([18,19,20,21,25,26,28,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,77,78,79,80,81,82,83,86,87,88,90,101,107,138,156,163,164,165,171,181,187,195,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,152,48,48,48,48,48,48,48,152,152,]),'TYPEOF':([18,19,20,21,25,26,28,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,77,78,79,80,81,82,83,86,87,88,90,101,138,156,163,164,165,171,181,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'PARDER':([19,22,23,27,29,30,31,32,33,34,35,36,51,52,53,54,55,57,73,74,75,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,125,126,127,128,129,130,134,135,136,137,148,155,157,158,159,160,161,162,166,167,168,173,174,175,176,183,184,185,186,],[50,56,-72,-63,-65,-66,-67,-68,-69,-70,-71,-73,89,-18,91,92,-14,105,-47,-48,122,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,155,157,158,159,160,161,162,166,167,168,-17,-13,-74,-76,-77,-78,-79,-80,-81,-85,-86,-87,183,184,185,186,-75,-82,-83,-84,]),'DOSPUNTOS':([23,24,27,29,30,31,32,33,34,35,36,58,73,74,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,155,157,158,159,160,161,162,166,167,168,169,177,182,183,184,185,186,191,],[-72,58,-63,-65,-66,-67,-68,-69,-70,-71,-73,107,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,-74,-76,-77,-78,-79,-80,-81,-85,-86,-87,177,187,191,-75,-82,-83,-84,195,]),'MAS':([23,24,27,29,30,31,32,33,34,35,36,52,53,54,73,74,75,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,134,135,136,137,145,155,157,158,159,160,161,162,166,167,168,169,173,174,175,176,182,183,184,185,186,190,],[-72,59,-63,-65,-66,-67,-68,-69,-70,-71,-73,59,59,59,-47,-48,59,-49,-50,-51,-52,-53,-54,59,59,59,59,59,59,59,59,-64,59,59,59,59,59,59,59,59,59,59,59,59,59,-74,-76,-77,-78,-79,-80,-81,-85,-86,-87,59,59,59,59,59,59,-75,-82,-83,-84,59,]),'MULT':([23,24,27,29,30,31,32,33,34,35,36,52,53,54,73,74,75,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,134,135,136,137,145,155,157,158,159,160,161,162,166,167,168,169,173,174,175,176,182,183,184,185,186,190,],[-72,61,-63,-65,-66,-67,-68,-69,-70,-71,-73,61,61,61,-47,-48,61,61,61,-51,-52,-53,-54,61,61,61,61,61,61,61,61,-64,61,61,61,61,61,61,61,61,61,61,61,61,61,-74,-76,-77,-78,-79,-80,-81,-85,-86,-87,61,61,61,61,61,61,-75,-82,-83,-84,61,]),'DIV':([23,24,27,29,30,31,32,33,34,35,36,52,53,54,73,74,75,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,134,135,136,137,145,155,157,158,159,160,161,162,166,167,168,169,173,174,175,176,182,183,184,185,186,190,],[-72,62,-63,-65,-66,-67,-68,-69,-70,-71,-73,62,62,62,-47,-48,62,62,62,-51,-52,-53,-54,62,62,62,62,62,62,62,62,-64,62,62,62,62,62,62,62,62,62,62,62,62,62,-74,-76,-77,-78,-79,-80,-81,-85,-86,-87,62,62,62,62,62,62,-75,-82,-83,-84,62,]),'MOD':([23,24,27,29,30,31,32,33,34,35,36,52,53,54,73,74,75,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,134,135,136,137,145,155,157,158,159,160,161,162,166,167,168,169,173,174,175,176,182,183,184,185,186,190,],[-72,63,-63,-65,-66,-67,-68,-69,-70,-71,-73,63,63,63,-47,-48,63,63,63,-51,-52,-53,-54,63,63,63,63,63,63,63,63,-64,63,63,63,63,63,63,63,63,63,63,63,63,63,-74,-76,-77,-78,-79,-80,-81,-85,-86,-87,63,63,63,63,63,63,-75,-82,-83,-84,63,]),'POT':([23,24,27,29,30,31,32,33,34,35,36,52,53,54,73,74,75,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,134,135,136,137,145,155,157,158,159,160,161,162,166,167,168,169,173,174,175,176,182,183,184,185,186,190,],[-72,64,-63,-65,-66,-67,-68,-69,-70,-71,-73,64,64,64,-47,-48,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,-64,64,64,64,64,64,64,64,64,64,64,64,64,64,-74,-76,-77,-78,-79,-80,-81,-85,-86,-87,64,64,64,64,64,64,-75,-82,-83,-84,64,]),'MAYOR':([23,24,27,29,30,31,32,33,34,35,36,52,53,54,73,74,75,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,134,135,136,137,145,155,157,158,159,160,161,162,166,167,168,169,173,174,175,176,182,183,184,185,186,190,],[-72,65,-63,-65,-66,-67,-68,-69,-70,-71,-73,65,65,65,-47,-48,65,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,65,65,65,65,-64,65,65,65,65,65,65,65,65,65,65,65,65,65,-74,-76,-77,-78,-79,-80,-81,-85,-86,-87,65,65,65,65,65,65,-75,-82,-83,-84,65,]),'MENOR':([23,24,27,29,30,31,32,33,34,35,36,52,53,54,73,74,75,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,134,135,136,137,145,155,157,158,159,160,161,162,166,167,168,169,173,174,175,176,182,183,184,185,186,190,],[-72,66,-63,-65,-66,-67,-68,-69,-70,-71,-73,66,66,66,-47,-48,66,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,66,66,66,66,-64,66,66,66,66,66,66,66,66,66,66,66,66,66,-74,-76,-77,-78,-79,-80,-81,-85,-86,-87,66,66,66,66,66,66,-75,-82,-83,-84,66,]),'MAYORIGUAL':([23,24,27,29,30,31,32,33,34,35,36,52,53,54,73,74,75,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,134,135,136,137,145,155,157,158,159,160,161,162,166,167,168,169,173,174,175,176,182,183,184,185,186,190,],[-72,67,-63,-65,-66,-67,-68,-69,-70,-71,-73,67,67,67,-47,-48,67,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,67,67,67,67,-64,67,67,67,67,67,67,67,67,67,67,67,67,67,-74,-76,-77,-78,-79,-80,-81,-85,-86,-87,67,67,67,67,67,67,-75,-82,-83,-84,67,]),'MENORIGUAL':([23,24,27,29,30,31,32,33,34,35,36,52,53,54,73,74,75,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,134,135,136,137,145,155,157,158,159,160,161,162,166,167,168,169,173,174,175,176,182,183,184,185,186,190,],[-72,68,-63,-65,-66,-67,-68,-69,-70,-71,-73,68,68,68,-47,-48,68,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,68,68,68,68,-64,68,68,68,68,68,68,68,68,68,68,68,68,68,-74,-76,-77,-78,-79,-80,-81,-85,-86,-87,68,68,68,68,68,68,-75,-82,-83,-84,68,]),'IGUALES':([23,24,27,29,30,31,32,33,34,35,36,52,53,54,73,74,75,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,134,135,136,137,145,155,157,158,159,160,161,162,166,167,168,169,173,174,175,176,182,183,184,185,186,190,],[-72,69,-63,-65,-66,-67,-68,-69,-70,-71,-73,69,69,69,-47,-48,69,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,69,69,-64,69,69,69,69,69,69,69,69,69,69,69,69,69,-74,-76,-77,-78,-79,-80,-81,-85,-86,-87,69,69,69,69,69,69,-75,-82,-83,-84,69,]),'DISTINTOS':([23,24,27,29,30,31,32,33,34,35,36,52,53,54,73,74,75,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,134,135,136,137,145,155,157,158,159,160,161,162,166,167,168,169,173,174,175,176,182,183,184,185,186,190,],[-72,70,-63,-65,-66,-67,-68,-69,-70,-71,-73,70,70,70,-47,-48,70,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,70,70,-64,70,70,70,70,70,70,70,70,70,70,70,70,70,-74,-76,-77,-78,-79,-80,-81,-85,-86,-87,70,70,70,70,70,70,-75,-82,-83,-84,70,]),'OR':([23,24,27,29,30,31,32,33,34,35,36,52,53,54,73,74,75,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,134,135,136,137,145,155,157,158,159,160,161,162,166,167,168,169,173,174,175,176,182,183,184,185,186,190,],[-72,71,-63,-65,-66,-67,-68,-69,-70,-71,-73,71,71,71,-47,-48,71,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,71,71,71,71,71,71,71,71,71,71,71,71,71,-74,-76,-77,-78,-79,-80,-81,-85,-86,-87,71,71,71,71,71,71,-75,-82,-83,-84,71,]),'AND':([23,24,27,29,30,31,32,33,34,35,36,52,53,54,73,74,75,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,134,135,136,137,145,155,157,158,159,160,161,162,166,167,168,169,173,174,175,176,182,183,184,185,186,190,],[-72,72,-63,-65,-66,-67,-68,-69,-70,-71,-73,72,72,72,-47,-48,72,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,72,-62,-64,72,72,72,72,72,72,72,72,72,72,72,72,72,-74,-76,-77,-78,-79,-80,-81,-85,-86,-87,72,72,72,72,72,72,-75,-82,-83,-84,72,]),'COMA':([23,27,29,30,31,32,33,34,35,36,51,52,55,57,73,74,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,124,131,132,133,137,148,155,157,158,159,160,161,162,166,167,168,183,184,185,186,],[-72,-63,-65,-66,-67,-68,-69,-70,-71,-73,90,-18,-14,106,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,156,163,164,165,-17,-13,-74,-76,-77,-78,-79,-80,-81,-85,-86,-87,-75,-82,-83,-84,]),'IF':([23,27,29,30,31,32,33,34,35,36,56,73,74,95,96,105,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,140,141,142,143,144,145,155,157,158,159,160,161,162,166,167,168,179,183,184,185,186,190,196,],[-72,-63,-65,-66,-67,-68,-69,-70,-71,-73,101,-47,-48,101,-20,101,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,-19,-21,-22,-23,-24,101,-74,-76,-77,-78,-79,-80,-81,-85,-86,-87,101,-75,-82,-83,-84,101,101,]),'LOCAL':([23,27,29,30,31,32,33,34,35,36,56,73,74,95,96,105,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,140,141,142,143,144,145,155,157,158,159,160,161,162,166,167,168,179,183,184,185,186,190,196,],[-72,-63,-65,-66,-67,-68,-69,-70,-71,-73,103,-47,-48,103,-20,103,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,-19,-21,-22,-23,-24,103,-74,-76,-77,-78,-79,-80,-81,-85,-86,-87,103,-75,-82,-83,-84,103,103,]),'GLOBAL':([23,27,29,30,31,32,33,34,35,36,56,73,74,95,96,105,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,140,141,142,143,144,145,155,157,158,159,160,161,162,166,167,168,179,183,184,185,186,190,196,],[-72,-63,-65,-66,-67,-68,-69,-70,-71,-73,104,-47,-48,104,-20,104,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,-19,-21,-22,-23,-24,104,-74,-76,-77,-78,-79,-80,-81,-85,-86,-87,104,-75,-82,-83,-84,104,104,]),'INT64':([84,85,107,187,195,],[131,133,150,150,150,]),'FLOAT64':([84,107,187,195,],[132,151,151,151,]),'END':([94,95,96,140,141,142,143,144,147,170,180,188,194,197,199,],[139,-25,-20,-19,-21,-22,-23,-24,172,178,189,193,-44,-46,-45,]),'ELSE':([95,96,140,141,142,143,144,170,194,],[-25,-20,-19,-21,-22,-23,-24,179,196,]),'ELSEIF':([95,96,140,141,142,143,144,170,194,],[-25,-20,-19,-21,-22,-23,-24,181,181,]),'BOOL':([107,187,195,],[153,153,153,]),'CHAR':([107,187,195,],[154,154,154,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'inicio':([0,],[1,]),'instruccionesglb':([0,],[2,]),'instruccionglb':([0,2,],[3,12,]),'funcionINS':([0,2,],[4,4,]),'declaracionglb':([0,2,],[5,5,]),'printINS':([0,2,56,95,105,145,179,190,196,],[6,6,97,97,97,97,97,97,97,]),'llamadaFunc':([0,2,56,95,105,145,179,190,196,],[7,7,100,100,100,100,100,100,100,]),'expresion':([18,19,20,21,25,26,28,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,77,78,79,80,81,82,83,86,87,88,90,101,138,156,163,164,165,171,181,],[24,52,53,54,73,74,75,108,109,110,111,112,113,114,115,116,117,118,119,120,121,123,124,125,126,127,128,129,130,134,135,136,137,145,169,173,174,175,176,182,190,]),'expValor':([18,19,20,21,25,26,28,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,77,78,79,80,81,82,83,86,87,88,90,101,138,156,163,164,165,171,181,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'expCHAR':([18,19,20,21,25,26,28,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,77,78,79,80,81,82,83,86,87,88,90,101,138,156,163,164,165,171,181,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'expNativas':([18,19,20,21,25,26,28,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,77,78,79,80,81,82,83,86,87,88,90,101,138,156,163,164,165,171,181,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'listParams':([19,],[51,]),'params':([22,],[57,]),'sentencia':([56,105,145,179,190,196,],[94,147,170,188,194,199,]),'instrucciones':([56,105,145,179,190,196,],[95,95,95,95,95,95,]),'instruccion':([56,95,105,145,179,190,196,],[96,140,96,96,96,96,96,]),'ifINS':([56,95,105,145,179,190,196,],[98,98,98,98,98,98,98,]),'declaracionINS':([56,95,105,145,179,190,196,],[99,99,99,99,99,99,99,]),'accesos':([56,95,105,145,179,190,196,],[102,102,102,102,102,102,102,]),'tipos':([107,187,195,],[149,192,198,]),'elseIfLista':([170,194,],[180,197,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> inicio","S'",1,None,None,None),
  ('inicio -> instruccionesglb','inicio',1,'p_start','Grammar.py',143),
  ('instruccionesglb -> instruccionesglb instruccionglb','instruccionesglb',2,'p_instruccionesglb','Grammar.py',149),
  ('instruccionesglb -> instruccionglb','instruccionesglb',1,'p_instruccionesglb','Grammar.py',150),
  ('instruccionglb -> funcionINS PUNTOCOMA','instruccionglb',2,'p_instruccionglb','Grammar.py',159),
  ('instruccionglb -> declaracionglb PUNTOCOMA','instruccionglb',2,'p_instruccionglb','Grammar.py',160),
  ('instruccionglb -> printINS PUNTOCOMA','instruccionglb',2,'p_instruccionglb','Grammar.py',161),
  ('instruccionglb -> llamadaFunc PUNTOCOMA','instruccionglb',2,'p_instruccionglb','Grammar.py',162),
  ('declaracionglb -> ID','declaracionglb',1,'p_declaracionglb','Grammar.py',167),
  ('declaracionglb -> ID IGUAL expresion','declaracionglb',3,'p_declaracionglb','Grammar.py',168),
  ('declaracionglb -> ID IGUAL expresion DOSPUNTOS DOSPUNTOS tipos','declaracionglb',6,'p_declaracionglb','Grammar.py',169),
  ('funcionINS -> FUNCTION ID PARIZQ PARDER sentencia END','funcionINS',6,'p_funcionINS','Grammar.py',179),
  ('funcionINS -> FUNCTION ID PARIZQ params PARDER sentencia END','funcionINS',7,'p_funcionINS','Grammar.py',180),
  ('params -> params COMA ID','params',3,'p_decParams','Grammar.py',188),
  ('params -> ID','params',1,'p_decParams','Grammar.py',189),
  ('llamadaFunc -> ID PARIZQ PARDER','llamadaFunc',3,'p_llamadaFunc','Grammar.py',198),
  ('llamadaFunc -> ID PARIZQ listParams PARDER','llamadaFunc',4,'p_llamadaFunc','Grammar.py',199),
  ('listParams -> listParams COMA expresion','listParams',3,'p_llamadaPar','Grammar.py',207),
  ('listParams -> expresion','listParams',1,'p_llamadaPar','Grammar.py',208),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones','Grammar.py',217),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones','Grammar.py',218),
  ('instruccion -> printINS PUNTOCOMA','instruccion',2,'p_instruccion','Grammar.py',227),
  ('instruccion -> ifINS PUNTOCOMA','instruccion',2,'p_instruccion','Grammar.py',228),
  ('instruccion -> declaracionINS PUNTOCOMA','instruccion',2,'p_instruccion','Grammar.py',229),
  ('instruccion -> llamadaFunc PUNTOCOMA','instruccion',2,'p_instruccion','Grammar.py',230),
  ('sentencia -> instrucciones','sentencia',1,'p_sentencia','Grammar.py',236),
  ('printINS -> PRINTLN PARIZQ expresion PARDER','printINS',4,'p_printlnINS','Grammar.py',242),
  ('printINS -> PRINT PARIZQ expresion PARDER','printINS',4,'p_printINS','Grammar.py',247),
  ('declaracionINS -> ID','declaracionINS',1,'p_declaracionINS','Grammar.py',252),
  ('declaracionINS -> ID IGUAL expresion','declaracionINS',3,'p_declaracionINS','Grammar.py',253),
  ('declaracionINS -> ID IGUAL expresion DOSPUNTOS DOSPUNTOS tipos','declaracionINS',6,'p_declaracionINS','Grammar.py',254),
  ('declaracionINS -> accesos ID','declaracionINS',2,'p_declaracionINS','Grammar.py',255),
  ('declaracionINS -> accesos ID IGUAL expresion','declaracionINS',4,'p_declaracionINS','Grammar.py',256),
  ('declaracionINS -> accesos ID IGUAL expresion DOSPUNTOS DOSPUNTOS tipos','declaracionINS',7,'p_declaracionINS','Grammar.py',257),
  ('tipos -> INT64','tipos',1,'p_tipos','Grammar.py',273),
  ('tipos -> FLOAT64','tipos',1,'p_tipos','Grammar.py',274),
  ('tipos -> STRING','tipos',1,'p_tipos','Grammar.py',275),
  ('tipos -> BOOL','tipos',1,'p_tipos','Grammar.py',276),
  ('tipos -> CHAR','tipos',1,'p_tipos','Grammar.py',277),
  ('accesos -> LOCAL','accesos',1,'p_accesos','Grammar.py',292),
  ('accesos -> GLOBAL','accesos',1,'p_accesos','Grammar.py',293),
  ('ifINS -> IF expresion sentencia END','ifINS',4,'p_ifINS','Grammar.py',303),
  ('ifINS -> IF expresion sentencia ELSE sentencia END','ifINS',6,'p_ifINS','Grammar.py',304),
  ('ifINS -> IF expresion sentencia elseIfLista END','ifINS',5,'p_ifINS','Grammar.py',305),
  ('elseIfLista -> ELSEIF expresion sentencia','elseIfLista',3,'p_elseIfLista','Grammar.py',315),
  ('elseIfLista -> ELSEIF expresion sentencia ELSE sentencia','elseIfLista',5,'p_elseIfLista','Grammar.py',316),
  ('elseIfLista -> ELSEIF expresion sentencia elseIfLista','elseIfLista',4,'p_elseIfLista','Grammar.py',317),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion','Grammar.py',327),
  ('expresion -> NOT expresion','expresion',2,'p_expresion','Grammar.py',328),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion','Grammar.py',330),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion','Grammar.py',331),
  ('expresion -> expresion MULT expresion','expresion',3,'p_expresion','Grammar.py',332),
  ('expresion -> expresion DIV expresion','expresion',3,'p_expresion','Grammar.py',333),
  ('expresion -> expresion MOD expresion','expresion',3,'p_expresion','Grammar.py',334),
  ('expresion -> expresion POT expresion','expresion',3,'p_expresion','Grammar.py',335),
  ('expresion -> expresion MAYOR expresion','expresion',3,'p_expresion','Grammar.py',337),
  ('expresion -> expresion MENOR expresion','expresion',3,'p_expresion','Grammar.py',338),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_expresion','Grammar.py',339),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresion','Grammar.py',340),
  ('expresion -> expresion IGUALES expresion','expresion',3,'p_expresion','Grammar.py',341),
  ('expresion -> expresion DISTINTOS expresion','expresion',3,'p_expresion','Grammar.py',342),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion','Grammar.py',344),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion','Grammar.py',345),
  ('expresion -> expValor','expresion',1,'p_expresion','Grammar.py',346),
  ('expValor -> PARIZQ expresion PARDER','expValor',3,'p_expValor','Grammar.py',387),
  ('expValor -> INTID','expValor',1,'p_expValor','Grammar.py',388),
  ('expValor -> FLOATID','expValor',1,'p_expValor','Grammar.py',389),
  ('expValor -> STRINGID','expValor',1,'p_expValor','Grammar.py',390),
  ('expValor -> expCHAR','expValor',1,'p_expValor','Grammar.py',391),
  ('expValor -> expNativas','expValor',1,'p_expValor','Grammar.py',392),
  ('expValor -> TRUE','expValor',1,'p_expValor','Grammar.py',393),
  ('expValor -> FALSE','expValor',1,'p_expValor','Grammar.py',394),
  ('expValor -> ID','expValor',1,'p_expValor','Grammar.py',395),
  ('expCHAR -> CHARID','expCHAR',1,'p_CHARS','Grammar.py',418),
  ('expNativas -> LOG10 PARIZQ expresion PARDER','expNativas',4,'p_defNativas','Grammar.py',423),
  ('expNativas -> LOG PARIZQ expresion COMA expresion PARDER','expNativas',6,'p_defNativas','Grammar.py',424),
  ('expNativas -> SIN PARIZQ expresion PARDER','expNativas',4,'p_defNativas','Grammar.py',425),
  ('expNativas -> COS PARIZQ expresion PARDER','expNativas',4,'p_defNativas','Grammar.py',426),
  ('expNativas -> TAN PARIZQ expresion PARDER','expNativas',4,'p_defNativas','Grammar.py',427),
  ('expNativas -> SQRT PARIZQ expresion PARDER','expNativas',4,'p_defNativas','Grammar.py',428),
  ('expNativas -> UPPERCASE PARIZQ expresion PARDER','expNativas',4,'p_defNativas','Grammar.py',429),
  ('expNativas -> LOWERCASE PARIZQ expresion PARDER','expNativas',4,'p_defNativas','Grammar.py',430),
  ('expNativas -> PARSE PARIZQ INT64 COMA expresion PARDER','expNativas',6,'p_defNativas','Grammar.py',431),
  ('expNativas -> PARSE PARIZQ FLOAT64 COMA expresion PARDER','expNativas',6,'p_defNativas','Grammar.py',432),
  ('expNativas -> TRUNC PARIZQ INT64 COMA expresion PARDER','expNativas',6,'p_defNativas','Grammar.py',433),
  ('expNativas -> FLOAT PARIZQ expresion PARDER','expNativas',4,'p_defNativas','Grammar.py',434),
  ('expNativas -> STRING PARIZQ expresion PARDER','expNativas',4,'p_defNativas','Grammar.py',435),
  ('expNativas -> TYPEOF PARIZQ expresion PARDER','expNativas',4,'p_defNativas','Grammar.py',436),
]
