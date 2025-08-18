package br.com.rengcarv.celular;

import br.com.rengcarv.calculadora.Calculadora;
import br.com.rengcarv.notificacao.Notificacoes;

public class Celular {

    public static void main(String[] args) {
        Notificacoes.notificar(String.valueOf(Calculadora.adicao(1, 2)));
    }
}
