
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftIGUALESDISTINTOSleftMAYORIGUALMENORIGUALMAYORMENORleftMASMENOSleftMULTDIVMODrightPOTrightNOTrightUMINUSleftPARIZQPARDERLLAVIZQLLAVDERAND BOOL CHAR CHARID COMA CORDER CORIZQ COS DISTINTOS DIV DOSPUNTOS ELSE ELSEIF END FALSE FLOAT FLOAT64 FLOATID ID IF IGUAL IGUALES INT64 INTID LLAVDER LLAVIZQ LOG LOG10 LOWERCASE MAS MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS MOD MULT NOT NULO OR PARDER PARIZQ PARSE POT PRINT PRINTLN PUNTO PUNTOCOMA SIN SQRT STRING STRINGID TAN TRUE TRUNC TYPEOF UPPERCASEinicio : instruccionesinstrucciones : instrucciones instruccion\n                    | instruccioninstruccion  : printINS PUNTOCOMA\n                    | ifINS PUNTOCOMAsentencia : instruccionesprintINS  : PRINTLN PARIZQ expresion PARDERprintINS  : PRINT PARIZQ expresion PARDERifINS : IF expresion sentencia END\n             | IF expresion sentencia ELSE sentencia END\n             | IF expresion sentencia elseIfLista ENDelseIfLista   : ELSEIF expresion sentencia\n                     | ELSEIF expresion sentencia ELSE sentencia\n                     | ELSEIF expresion sentencia elseIfListaexpresion    : MENOS expresion %prec UMINUS\n                    | NOT expresion %prec UMINUS\n\n                    | expresion MAS expresion\n                    | expresion MENOS expresion\n                    | expresion MULT expresion\n                    | expresion DIV expresion\n                    | expresion MOD expresion\n                    | expresion POT expresion\n\n                    | expresion MAYOR expresion\n                    | expresion MENOR expresion\n                    | expresion MAYORIGUAL expresion\n                    | expresion MENORIGUAL expresion\n                    | expresion IGUALES expresion\n                    | expresion DISTINTOS expresion\n\n                    | expresion OR expresion\n                    | expresion AND expresion\n                    | expValorexpValor : PARIZQ expresion PARDER\n                | INTID\n                | FLOATID\n                | STRINGID\n                | expCHAR\n                | expNativas\n                | TRUE\n                | FALSEexpCHAR : CHARIDexpNativas : LOG10 PARIZQ expresion PARDER\n                  | LOG PARIZQ expresion COMA expresion PARDER\n                  | SIN PARIZQ expresion PARDER\n                  | COS PARIZQ expresion PARDER\n                  | TAN PARIZQ expresion PARDER\n                  | SQRT PARIZQ expresion PARDER\n                  | UPPERCASE PARIZQ expresion PARDER\n                  | LOWERCASE PARIZQ expresion PARDER\n                  | PARSE PARIZQ INT64 COMA expresion PARDER\n                  | PARSE PARIZQ FLOAT64 COMA expresion PARDER\n                  | TRUNC PARIZQ INT64 COMA expresion PARDER\n                  | FLOAT PARIZQ expresion PARDER\n                  | STRING PARIZQ expresion PARDER\n                  | TYPEOF PARIZQ expresion PARDER'
    
_lr_action_items = {'PRINTLN':([0,2,3,9,10,11,14,17,19,20,21,22,23,24,25,26,57,58,59,77,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,111,112,114,115,116,117,118,119,123,124,125,132,134,135,136,137,],[6,6,-3,-2,-4,-5,6,-31,-33,-34,-35,-36,-37,-38,-39,-40,6,-15,-16,6,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-32,6,-41,-43,-44,-45,-46,-47,-48,-52,-53,-54,6,-42,-49,-50,-51,]),'PRINT':([0,2,3,9,10,11,14,17,19,20,21,22,23,24,25,26,57,58,59,77,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,111,112,114,115,116,117,118,119,123,124,125,132,134,135,136,137,],[7,7,-3,-2,-4,-5,7,-31,-33,-34,-35,-36,-37,-38,-39,-40,7,-15,-16,7,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-32,7,-41,-43,-44,-45,-46,-47,-48,-52,-53,-54,7,-42,-49,-50,-51,]),'IF':([0,2,3,9,10,11,14,17,19,20,21,22,23,24,25,26,57,58,59,77,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,111,112,114,115,116,117,118,119,123,124,125,132,134,135,136,137,],[8,8,-3,-2,-4,-5,8,-31,-33,-34,-35,-36,-37,-38,-39,-40,8,-15,-16,8,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-32,8,-41,-43,-44,-45,-46,-47,-48,-52,-53,-54,8,-42,-49,-50,-51,]),'$end':([1,2,3,9,10,11,],[0,-1,-3,-2,-4,-5,]),'END':([3,9,10,11,42,57,78,109,127,133,138,],[-3,-2,-4,-5,76,-6,110,126,-12,-14,-13,]),'ELSE':([3,9,10,11,42,57,127,],[-3,-2,-4,-5,77,-6,132,]),'ELSEIF':([3,9,10,11,42,57,127,],[-3,-2,-4,-5,79,-6,79,]),'PUNTOCOMA':([4,5,74,75,76,110,126,],[10,11,-7,-8,-9,-11,-10,]),'PARIZQ':([6,7,8,12,13,15,16,18,27,28,29,30,31,32,33,34,35,36,37,38,39,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,71,72,73,79,113,120,121,122,],[12,13,18,18,18,18,18,18,61,62,63,64,65,66,67,68,69,70,71,72,73,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'MENOS':([8,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,58,59,60,61,62,63,64,65,66,67,68,71,72,73,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,106,107,108,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,128,129,130,131,134,135,136,137,],[15,15,15,44,15,15,-31,15,-33,-34,-35,-36,-37,-38,-39,-40,44,44,15,15,15,15,15,15,15,15,15,15,15,15,15,15,-15,-16,44,15,15,15,15,15,15,15,15,15,15,15,15,-17,-18,-19,-20,-21,-22,44,44,44,44,44,44,44,44,-32,44,44,44,44,44,44,44,44,44,44,44,44,-41,15,-43,-44,-45,-46,-47,-48,15,15,15,-52,-53,-54,44,44,44,44,-42,-49,-50,-51,]),'NOT':([8,12,13,15,16,18,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,71,72,73,79,113,120,121,122,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'INTID':([8,12,13,15,16,18,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,71,72,73,79,113,120,121,122,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'FLOATID':([8,12,13,15,16,18,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,71,72,73,79,113,120,121,122,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'STRINGID':([8,12,13,15,16,18,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,71,72,73,79,113,120,121,122,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'TRUE':([8,12,13,15,16,18,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,71,72,73,79,113,120,121,122,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'FALSE':([8,12,13,15,16,18,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,71,72,73,79,113,120,121,122,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'CHARID':([8,12,13,15,16,18,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,71,72,73,79,113,120,121,122,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'LOG10':([8,12,13,15,16,18,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,71,72,73,79,113,120,121,122,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'LOG':([8,12,13,15,16,18,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,71,72,73,79,113,120,121,122,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'SIN':([8,12,13,15,16,18,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,71,72,73,79,113,120,121,122,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'COS':([8,12,13,15,16,18,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,71,72,73,79,113,120,121,122,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'TAN':([8,12,13,15,16,18,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,71,72,73,79,113,120,121,122,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'SQRT':([8,12,13,15,16,18,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,71,72,73,79,113,120,121,122,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'UPPERCASE':([8,12,13,15,16,18,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,71,72,73,79,113,120,121,122,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'LOWERCASE':([8,12,13,15,16,18,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,71,72,73,79,113,120,121,122,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'PARSE':([8,12,13,15,16,18,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,71,72,73,79,113,120,121,122,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'TRUNC':([8,12,13,15,16,18,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,71,72,73,79,113,120,121,122,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'FLOAT':([8,12,13,15,16,18,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,71,72,73,79,113,120,121,122,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'STRING':([8,12,13,15,16,18,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,71,72,73,79,113,120,121,122,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'TYPEOF':([8,12,13,15,16,18,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,71,72,73,79,113,120,121,122,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'MAS':([14,17,19,20,21,22,23,24,25,26,40,41,58,59,60,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,106,107,108,111,112,114,115,116,117,118,119,123,124,125,128,129,130,131,134,135,136,137,],[43,-31,-33,-34,-35,-36,-37,-38,-39,-40,43,43,-15,-16,43,-17,-18,-19,-20,-21,-22,43,43,43,43,43,43,43,43,-32,43,43,43,43,43,43,43,43,43,43,43,43,-41,-43,-44,-45,-46,-47,-48,-52,-53,-54,43,43,43,43,-42,-49,-50,-51,]),'MULT':([14,17,19,20,21,22,23,24,25,26,40,41,58,59,60,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,106,107,108,111,112,114,115,116,117,118,119,123,124,125,128,129,130,131,134,135,136,137,],[45,-31,-33,-34,-35,-36,-37,-38,-39,-40,45,45,-15,-16,45,45,45,-19,-20,-21,-22,45,45,45,45,45,45,45,45,-32,45,45,45,45,45,45,45,45,45,45,45,45,-41,-43,-44,-45,-46,-47,-48,-52,-53,-54,45,45,45,45,-42,-49,-50,-51,]),'DIV':([14,17,19,20,21,22,23,24,25,26,40,41,58,59,60,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,106,107,108,111,112,114,115,116,117,118,119,123,124,125,128,129,130,131,134,135,136,137,],[46,-31,-33,-34,-35,-36,-37,-38,-39,-40,46,46,-15,-16,46,46,46,-19,-20,-21,-22,46,46,46,46,46,46,46,46,-32,46,46,46,46,46,46,46,46,46,46,46,46,-41,-43,-44,-45,-46,-47,-48,-52,-53,-54,46,46,46,46,-42,-49,-50,-51,]),'MOD':([14,17,19,20,21,22,23,24,25,26,40,41,58,59,60,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,106,107,108,111,112,114,115,116,117,118,119,123,124,125,128,129,130,131,134,135,136,137,],[47,-31,-33,-34,-35,-36,-37,-38,-39,-40,47,47,-15,-16,47,47,47,-19,-20,-21,-22,47,47,47,47,47,47,47,47,-32,47,47,47,47,47,47,47,47,47,47,47,47,-41,-43,-44,-45,-46,-47,-48,-52,-53,-54,47,47,47,47,-42,-49,-50,-51,]),'POT':([14,17,19,20,21,22,23,24,25,26,40,41,58,59,60,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,106,107,108,111,112,114,115,116,117,118,119,123,124,125,128,129,130,131,134,135,136,137,],[48,-31,-33,-34,-35,-36,-37,-38,-39,-40,48,48,-15,-16,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-32,48,48,48,48,48,48,48,48,48,48,48,48,-41,-43,-44,-45,-46,-47,-48,-52,-53,-54,48,48,48,48,-42,-49,-50,-51,]),'MAYOR':([14,17,19,20,21,22,23,24,25,26,40,41,58,59,60,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,106,107,108,111,112,114,115,116,117,118,119,123,124,125,128,129,130,131,134,135,136,137,],[49,-31,-33,-34,-35,-36,-37,-38,-39,-40,49,49,-15,-16,49,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,49,49,49,49,-32,49,49,49,49,49,49,49,49,49,49,49,49,-41,-43,-44,-45,-46,-47,-48,-52,-53,-54,49,49,49,49,-42,-49,-50,-51,]),'MENOR':([14,17,19,20,21,22,23,24,25,26,40,41,58,59,60,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,106,107,108,111,112,114,115,116,117,118,119,123,124,125,128,129,130,131,134,135,136,137,],[50,-31,-33,-34,-35,-36,-37,-38,-39,-40,50,50,-15,-16,50,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,50,50,50,50,-32,50,50,50,50,50,50,50,50,50,50,50,50,-41,-43,-44,-45,-46,-47,-48,-52,-53,-54,50,50,50,50,-42,-49,-50,-51,]),'MAYORIGUAL':([14,17,19,20,21,22,23,24,25,26,40,41,58,59,60,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,106,107,108,111,112,114,115,116,117,118,119,123,124,125,128,129,130,131,134,135,136,137,],[51,-31,-33,-34,-35,-36,-37,-38,-39,-40,51,51,-15,-16,51,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,51,51,51,51,-32,51,51,51,51,51,51,51,51,51,51,51,51,-41,-43,-44,-45,-46,-47,-48,-52,-53,-54,51,51,51,51,-42,-49,-50,-51,]),'MENORIGUAL':([14,17,19,20,21,22,23,24,25,26,40,41,58,59,60,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,106,107,108,111,112,114,115,116,117,118,119,123,124,125,128,129,130,131,134,135,136,137,],[52,-31,-33,-34,-35,-36,-37,-38,-39,-40,52,52,-15,-16,52,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,52,52,52,52,-32,52,52,52,52,52,52,52,52,52,52,52,52,-41,-43,-44,-45,-46,-47,-48,-52,-53,-54,52,52,52,52,-42,-49,-50,-51,]),'IGUALES':([14,17,19,20,21,22,23,24,25,26,40,41,58,59,60,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,106,107,108,111,112,114,115,116,117,118,119,123,124,125,128,129,130,131,134,135,136,137,],[53,-31,-33,-34,-35,-36,-37,-38,-39,-40,53,53,-15,-16,53,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,53,53,-32,53,53,53,53,53,53,53,53,53,53,53,53,-41,-43,-44,-45,-46,-47,-48,-52,-53,-54,53,53,53,53,-42,-49,-50,-51,]),'DISTINTOS':([14,17,19,20,21,22,23,24,25,26,40,41,58,59,60,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,106,107,108,111,112,114,115,116,117,118,119,123,124,125,128,129,130,131,134,135,136,137,],[54,-31,-33,-34,-35,-36,-37,-38,-39,-40,54,54,-15,-16,54,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,54,54,-32,54,54,54,54,54,54,54,54,54,54,54,54,-41,-43,-44,-45,-46,-47,-48,-52,-53,-54,54,54,54,54,-42,-49,-50,-51,]),'OR':([14,17,19,20,21,22,23,24,25,26,40,41,58,59,60,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,106,107,108,111,112,114,115,116,117,118,119,123,124,125,128,129,130,131,134,135,136,137,],[55,-31,-33,-34,-35,-36,-37,-38,-39,-40,55,55,-15,-16,55,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-32,55,55,55,55,55,55,55,55,55,55,55,55,-41,-43,-44,-45,-46,-47,-48,-52,-53,-54,55,55,55,55,-42,-49,-50,-51,]),'AND':([14,17,19,20,21,22,23,24,25,26,40,41,58,59,60,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,106,107,108,111,112,114,115,116,117,118,119,123,124,125,128,129,130,131,134,135,136,137,],[56,-31,-33,-34,-35,-36,-37,-38,-39,-40,56,56,-15,-16,56,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,56,-30,-32,56,56,56,56,56,56,56,56,56,56,56,56,-41,-43,-44,-45,-46,-47,-48,-52,-53,-54,56,56,56,56,-42,-49,-50,-51,]),'PARDER':([17,19,20,21,22,23,24,25,26,40,41,58,59,60,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,99,100,101,102,106,107,108,112,114,115,116,117,118,119,123,124,125,128,129,130,131,134,135,136,137,],[-31,-33,-34,-35,-36,-37,-38,-39,-40,74,75,-15,-16,94,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-32,112,114,115,116,117,118,119,123,124,125,-41,-43,-44,-45,-46,-47,-48,-52,-53,-54,134,135,136,137,-42,-49,-50,-51,]),'COMA':([17,19,20,21,22,23,24,25,26,58,59,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,96,103,104,105,112,114,115,116,117,118,119,123,124,125,134,135,136,137,],[-31,-33,-34,-35,-36,-37,-38,-39,-40,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-32,113,120,121,122,-41,-43,-44,-45,-46,-47,-48,-52,-53,-54,-42,-49,-50,-51,]),'INT64':([69,70,],[103,105,]),'FLOAT64':([69,],[104,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'inicio':([0,],[1,]),'instrucciones':([0,14,77,111,132,],[2,57,57,57,57,]),'instruccion':([0,2,14,57,77,111,132,],[3,9,3,9,3,3,3,]),'printINS':([0,2,14,57,77,111,132,],[4,4,4,4,4,4,4,]),'ifINS':([0,2,14,57,77,111,132,],[5,5,5,5,5,5,5,]),'expresion':([8,12,13,15,16,18,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,71,72,73,79,113,120,121,122,],[14,40,41,58,59,60,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,99,100,101,102,106,107,108,111,128,129,130,131,]),'expValor':([8,12,13,15,16,18,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,71,72,73,79,113,120,121,122,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'expCHAR':([8,12,13,15,16,18,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,71,72,73,79,113,120,121,122,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'expNativas':([8,12,13,15,16,18,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,71,72,73,79,113,120,121,122,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'sentencia':([14,77,111,132,],[42,109,127,138,]),'elseIfLista':([42,127,],[78,133,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> inicio","S'",1,None,None,None),
  ('inicio -> instrucciones','inicio',1,'p_start','Grammar.py',137),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones','Grammar.py',143),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones','Grammar.py',144),
  ('instruccion -> printINS PUNTOCOMA','instruccion',2,'p_instruccion','Grammar.py',153),
  ('instruccion -> ifINS PUNTOCOMA','instruccion',2,'p_instruccion','Grammar.py',154),
  ('sentencia -> instrucciones','sentencia',1,'p_sentencia','Grammar.py',160),
  ('printINS -> PRINTLN PARIZQ expresion PARDER','printINS',4,'p_printlnINS','Grammar.py',166),
  ('printINS -> PRINT PARIZQ expresion PARDER','printINS',4,'p_printINS','Grammar.py',171),
  ('ifINS -> IF expresion sentencia END','ifINS',4,'p_ifINS','Grammar.py',177),
  ('ifINS -> IF expresion sentencia ELSE sentencia END','ifINS',6,'p_ifINS','Grammar.py',178),
  ('ifINS -> IF expresion sentencia elseIfLista END','ifINS',5,'p_ifINS','Grammar.py',179),
  ('elseIfLista -> ELSEIF expresion sentencia','elseIfLista',3,'p_elseIfLista','Grammar.py',189),
  ('elseIfLista -> ELSEIF expresion sentencia ELSE sentencia','elseIfLista',5,'p_elseIfLista','Grammar.py',190),
  ('elseIfLista -> ELSEIF expresion sentencia elseIfLista','elseIfLista',4,'p_elseIfLista','Grammar.py',191),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion','Grammar.py',201),
  ('expresion -> NOT expresion','expresion',2,'p_expresion','Grammar.py',202),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion','Grammar.py',204),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion','Grammar.py',205),
  ('expresion -> expresion MULT expresion','expresion',3,'p_expresion','Grammar.py',206),
  ('expresion -> expresion DIV expresion','expresion',3,'p_expresion','Grammar.py',207),
  ('expresion -> expresion MOD expresion','expresion',3,'p_expresion','Grammar.py',208),
  ('expresion -> expresion POT expresion','expresion',3,'p_expresion','Grammar.py',209),
  ('expresion -> expresion MAYOR expresion','expresion',3,'p_expresion','Grammar.py',211),
  ('expresion -> expresion MENOR expresion','expresion',3,'p_expresion','Grammar.py',212),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_expresion','Grammar.py',213),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresion','Grammar.py',214),
  ('expresion -> expresion IGUALES expresion','expresion',3,'p_expresion','Grammar.py',215),
  ('expresion -> expresion DISTINTOS expresion','expresion',3,'p_expresion','Grammar.py',216),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion','Grammar.py',218),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion','Grammar.py',219),
  ('expresion -> expValor','expresion',1,'p_expresion','Grammar.py',220),
  ('expValor -> PARIZQ expresion PARDER','expValor',3,'p_expValor','Grammar.py',261),
  ('expValor -> INTID','expValor',1,'p_expValor','Grammar.py',262),
  ('expValor -> FLOATID','expValor',1,'p_expValor','Grammar.py',263),
  ('expValor -> STRINGID','expValor',1,'p_expValor','Grammar.py',264),
  ('expValor -> expCHAR','expValor',1,'p_expValor','Grammar.py',265),
  ('expValor -> expNativas','expValor',1,'p_expValor','Grammar.py',266),
  ('expValor -> TRUE','expValor',1,'p_expValor','Grammar.py',267),
  ('expValor -> FALSE','expValor',1,'p_expValor','Grammar.py',268),
  ('expCHAR -> CHARID','expCHAR',1,'p_CHARS','Grammar.py',289),
  ('expNativas -> LOG10 PARIZQ expresion PARDER','expNativas',4,'p_defNativas','Grammar.py',294),
  ('expNativas -> LOG PARIZQ expresion COMA expresion PARDER','expNativas',6,'p_defNativas','Grammar.py',295),
  ('expNativas -> SIN PARIZQ expresion PARDER','expNativas',4,'p_defNativas','Grammar.py',296),
  ('expNativas -> COS PARIZQ expresion PARDER','expNativas',4,'p_defNativas','Grammar.py',297),
  ('expNativas -> TAN PARIZQ expresion PARDER','expNativas',4,'p_defNativas','Grammar.py',298),
  ('expNativas -> SQRT PARIZQ expresion PARDER','expNativas',4,'p_defNativas','Grammar.py',299),
  ('expNativas -> UPPERCASE PARIZQ expresion PARDER','expNativas',4,'p_defNativas','Grammar.py',300),
  ('expNativas -> LOWERCASE PARIZQ expresion PARDER','expNativas',4,'p_defNativas','Grammar.py',301),
  ('expNativas -> PARSE PARIZQ INT64 COMA expresion PARDER','expNativas',6,'p_defNativas','Grammar.py',302),
  ('expNativas -> PARSE PARIZQ FLOAT64 COMA expresion PARDER','expNativas',6,'p_defNativas','Grammar.py',303),
  ('expNativas -> TRUNC PARIZQ INT64 COMA expresion PARDER','expNativas',6,'p_defNativas','Grammar.py',304),
  ('expNativas -> FLOAT PARIZQ expresion PARDER','expNativas',4,'p_defNativas','Grammar.py',305),
  ('expNativas -> STRING PARIZQ expresion PARDER','expNativas',4,'p_defNativas','Grammar.py',306),
  ('expNativas -> TYPEOF PARIZQ expresion PARDER','expNativas',4,'p_defNativas','Grammar.py',307),
]
