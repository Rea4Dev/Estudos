package br.com.rengcarv.relogio;

public class Depertador {
    public static void main(String[] args) {
        String mensagemDaFunção = agendarAlarme(12, 30);
        System.out.println(mensagemDaFunção);
    }

    public static String agendarAlarme(int hora, int min){
        return "Alarme agendado para " + hora + ":" + min;
    }
}