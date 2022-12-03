using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MOD9_Exer4
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Empregado E1 = new Empregado("Martim", 16, 1500.70);
            E1.MostrarDados();
            Console.ReadLine();
        }
    }
}
