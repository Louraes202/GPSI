using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MOD9_Exer4
{
    internal class Empregado
    {
        private string nome;
        private int idade;
        private double salario;
        public Empregado ()
        {
            nome = "";
            idade = 0;
            salario = 0;
        }

        public Empregado (string nome, int idade, double salario)
        {
            this.nome = nome;
            this.idade = idade;
            this.salario = salario;
        }

        public string Nome()
        {
            return this.nome;
        }

        public int Idade()
        {
            return this.idade;
        }

        public double Salario()
        {
            return this.salario;
        }

        public void MostrarDados()
        {
            Console.WriteLine("Empregado {0}, tem {1} anos e recebe {2} por mês.", nome, idade, salario);
        }
    }
}
