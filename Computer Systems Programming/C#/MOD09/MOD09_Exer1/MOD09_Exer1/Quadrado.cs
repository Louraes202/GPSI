using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MOD09_Exer1
{
    internal class Quadrado
    {
        private double lado;
        public Quadrado() // Construtor vazio
        {
            this.lado = 1.0;
        }

        public Quadrado(double lado) // Construtor com parâmetros
        {
            this.lado = lado;
        }

        public double area() // Area
        {
            double area = 2 * lado;
            return area;
        }

        public double diagonal() // Diagonal
        {
            double diagonal = Math.Sqrt(2 * lado);
            return diagonal;
        }

        public double perimetro() // Perimetro
        {
            double perimetro = 4 * lado;
            return perimetro;
        }
    }
}
