package br.com.rengcarv.banco;

public class ContaBancaria{
	public static void main(String[] args){
		private String numero = "0";
		private String titular;
		private double saldo;
	}

	public ContaBancaria(String numero, String titular, double saldoInicial){
		
		if(numero == null || numero.isBlank()){
			throw new IllegalArgumentException("Numero não pode ser vazio!");
		}

		this.numero = numero;
		this.titular = titular;
		this.saldo = saldoInicial;
	}
}
