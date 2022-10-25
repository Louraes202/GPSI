using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MOD09_Exer3
{
    class BilheteVIP : Bilhete
    {
        double valorAdicional;
        double valorTotal;

        public BilheteVIP() { 
        }

        public BilheteVIP(double valorAdicional, Bilhete novobilhete) : base()
        {
            valorTotal = valorAdicional + novobilhete.imprimirValor();
        }

        public double imprimirTotal() {
            return valorTotal;
        }
    }
}
