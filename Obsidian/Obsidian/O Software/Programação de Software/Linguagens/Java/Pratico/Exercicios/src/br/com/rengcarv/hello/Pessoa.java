package br.com.rengcarv.hello;

public class Pessoa{
    String nome;
    int idade;

    public void criar(String nome, int idade){
        this.nome = nome;
        this.idade = idade;
    }

    public String toString(){
        String texto = "Sou " + nome + " e tenho " + idade + " anos";
        return texto;
    }
}