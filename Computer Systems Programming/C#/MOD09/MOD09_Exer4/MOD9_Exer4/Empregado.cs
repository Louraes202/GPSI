using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MOD9_Exer4
{
    class Empregado
    {
        private string nome;
        private double salario;

        public Empregado()
        {
            nome = "";
            salario = 0;
        }
        public Empregado(string _nome, double _salario)
        {
            nome = _nome;
            salario = _salario;
        }

        public void MostrarDados()
        {
            Console.WriteLine("{0}, {1}", nome, salario);
        }

        public string Nome()
        {
            return nome;
        }

        public double Salario()
        {
            return salario;
        }



    }

   
}
