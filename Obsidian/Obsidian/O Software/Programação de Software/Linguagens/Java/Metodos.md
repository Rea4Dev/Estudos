---
data_criacao: 12-08-2025
flashcards: Não feito
revisão: Não feita
---
```Java
public class Depertador{

    public static void main(String[] args) {
        String mensagemDaFunção = agendarAlarme(12, 30);
        System.out.println(mensagemDaFunção);
    }

    public static String agendarAlarme(int hora, int min){
        return "Alarme agendado para " + hora + ":" + min;
    }
}
```