package br.com.fiap.bean;

public class Paciente extends Prontuario {
    private String nome;
    private String cpf;
    private String dataNascimento;

    public Paciente(String nome, String cpf, String dataNascimento, String numeroProntuario) {
        super(numeroProntuario);
        this.nome = nome;
        this.cpf = cpf;
        this.dataNascimento = dataNascimento;
    }

    public String getNome() {
        return nome;
    }

    public String getCpf() {
        return cpf;
    }

    public String getDataNascimento() {
        return dataNascimento;
    }
}