using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MOD09_Exer1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            double lado;
            Console.WriteLine("Lado do quadrado: ");
            bool doublelado = double.TryParse(Console.ReadLine(), out lado);
            while (doublelado == false)
            {
                Console.WriteLine("O lado tem de ser um valor real!");
                Console.WriteLine("Lado do quadrado: ");
                doublelado = double.TryParse(Console.ReadLine(), out lado);
            }

            if (lado >= 0 && lado <= 20)
            {
                Quadrado quadrado1 = new Quadrado(lado);
                Console.WriteLine("Area do Quadrado: " + quadrado1.area());
                Console.WriteLine("Diagonal do Quadrado: " + quadrado1.diagonal());
                Console.WriteLine("Perímetro do Quadrado: " + quadrado1.perimetro());
                Console.ReadLine();
            }
            else if (lado < 0 || lado > 20) {
                while (lado < 0 || lado > 20)
                {
                    Console.WriteLine("O valor do lado tem de ser um valor real entre entre 0 e 20.");
                    Console.WriteLine("Lado do quadrado: ");
                    doublelado = double.TryParse(Console.ReadLine(), out lado);
                    while (doublelado == false)
                    {
                        Console.WriteLine("O lado tem de ser um valor real!");
                        Console.WriteLine("Lado do quadrado: ");
                        doublelado = double.TryParse(Console.ReadLine(), out lado);
                    }
                }
                Quadrado quadrado1 = new Quadrado(lado);
                Console.WriteLine("Area do Quadrado: " + quadrado1.area());
                Console.WriteLine("Diagonal do Quadrado: " + quadrado1.diagonal());
                Console.WriteLine("Perímetro do Quadrado: " + quadrado1.perimetro());
                Console.ReadLine();
            }
            
                                 
        }
    }
}
