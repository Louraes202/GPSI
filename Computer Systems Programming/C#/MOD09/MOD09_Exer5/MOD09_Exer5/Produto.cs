using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MOD09_Exer5
{
    class Produto
    {
        string nome;
        double precoCusto;
        double precoVenda;
        double margemLucro;

        public Produto()
        {
            nome = "";
            precoCusto = 0;
            precoVenda = 0;
            margemLucro = 0;
        }

        public Produto(string a, double b, double c)
        {
            this.nome = a;
            this.precoCusto = b;
            this.precoVenda = c;
        }

        public void change_precoCusto(double a)
        {
            this.precoCusto = a;
        }

        public void change_precoVenda(double a)
        {
            this.precoVenda = a;
        }


        public double getPrecoCusto()
        {
            return this.precoCusto;
        }

        public double getPrecoVenda()
        {
            return this.precoVenda;
        }
        public double calcularMargemLucro()
        {
            this.margemLucro = this.precoVenda - this.precoCusto;
            return margemLucro;
        }

        public double getMargemLucroPercentagem()
        {
            double permargemLucro = (margemLucro * 100) / precoCusto;
            return permargemLucro;
        }
    }
}
