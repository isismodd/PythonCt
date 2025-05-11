package br.com.fiap.bean;

public class Medico {
    private String nome;
    private String crm;
    private AreaAtuacao especialidade;

    public Medico(String nome, String crm, AreaAtuacao especialidade) {
        this.nome = nome;
        this.crm = crm;
        this.especialidade = especialidade;
    }

    public String getNome() {
        return nome;
    }

    public String getCrm() {
        return crm;
    }

    public AreaAtuacao getEspecialidade() {
        return especialidade;
    }
}