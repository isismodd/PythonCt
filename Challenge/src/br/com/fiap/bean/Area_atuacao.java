package br.com.fiap.bean;

public class AreaAtuacao {
    // Constantes que substituem os valores do enum
    public static final AreaAtuacao CARDIOLOGIA = new AreaAtuacao("Cardiologia");
    public static final AreaAtuacao ORTOPEDIA = new AreaAtuacao("Ortopedia");
    public static final AreaAtuacao PEDIATRIA = new AreaAtuacao("Pediatria");
    // ... adicione as outras áreas

    private String nome;

    // Construtor privado para evitar novas instâncias
    private AreaAtuacao(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    // Método para obter todas as áreas disponíveis
    public static AreaAtuacao[] values() {
        return new AreaAtuacao[] {
            CARDIOLOGIA,
            ORTOPEDIA,
            PEDIATRIA,
            // ... outras áreas
        };
    }
}
