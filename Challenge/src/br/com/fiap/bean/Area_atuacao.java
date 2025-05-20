package br.com.fiap.bean;

public class AreaAtuacao {

    public static final AreaAtuacao CARDIOLOGIA = new AreaAtuacao("Cardiologia");
    public static final AreaAtuacao ORTOPEDIA = new AreaAtuacao("Ortopedia");
    public static final AreaAtuacao PEDIATRIA = new AreaAtuacao("Pediatria");


    private String nome;

  
    private AreaAtuacao(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

   
    public static AreaAtuacao[] values() {
        return new AreaAtuacao[] {
            CARDIOLOGIA,
            ORTOPEDIA,
            PEDIATRIA,
    
        };
    }
}
