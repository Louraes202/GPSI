﻿// See https://aka.ms/new-console-template for more information
using MOD09_Exer3;

Bilhete b1 = new Bilhete(50);
BilheteVIP b2 = new BilheteVIP(20, b1);


Console.WriteLine(b2.imprimirTotal());
Console.WriteLine(b1.imprimirValor());

double diferenca = b2.imprimirTotal() - b1.imprimirValor();




Console.WriteLine("A diferença dos bilhetes será de {0} euros", diferenca);