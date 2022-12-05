using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MOD9_Exer2
{
    class Pessoa
    {
        // valores
        public string nome;
        public string datanascimento;
        public double altura;

        // metodos
        public Pessoa()
        {
            nome = "";
            datanascimento = "";
            altura = 0;
        }

        public Pessoa(string nome, string datanascimento, double altura)
        {
            this.nome = nome;
            this.datanascimento = datanascimento;
            this.altura = altura;
        }

    }
}
