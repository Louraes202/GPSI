using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MOD09_Exer3
{
    public class Bilhete
    {
        double valor;

        public Bilhete()
        {

        }

        public Bilhete(double nvalor)
        {
            this.valor = nvalor;
        }

        public double imprimirValor()
        {
            return valor;
        }
    }
}
