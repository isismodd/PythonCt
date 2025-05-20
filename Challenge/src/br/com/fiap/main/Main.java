package br.com.fiap.main;

import br.com.fiap.bean.*;
import java.util.Date;

public class Main {
    public static void main(String[] args) {
        // Criando hospital
        Hospital hospital = new Hospital("Hospital das Clínicas Central");

        // Criando unidades
        Unidade unidade1 = new Unidade("Unidade Centro", "Rua Principal, 100");
        Unidade unidade2 = new Unidade("Unidade Zona Norte", "Av. Secundária, 200");
        hospital.adicionarUnidade(unidade1);
        hospital.adicionarUnidade(unidade2);

        // Criando médicos usando a classe AreaAtuacao
        Medico cirurgiao = new Medico(
            "Dr. Silva", 
            "CRM/SP 12345", 
            AreaAtuacao.CIRURGIAO  /
        );
        
        Medico cardiologista = new Medico(
            "Dra. Oliveira", 
            "CRM/SP 54321", 
            AreaAtuacao.CARDIOLOGIA 
        );

        unidade1.adicionarMedico(cirurgiao);
        unidade2.adicionarMedico(cardioloista);

        // Criando aplicativo
        Aplicativo app = new Aplicativo(hospital);

        // Cadastrando pacientes
        Paciente paciente1 = new Paciente("João da Silva", "111.222.333-44", "15/05/1980", "P20230001");
        Paciente paciente2 = new Paciente("Maria Souza", "222.333.444-55", "20/11/1990", "P20230002");
        app.cadastrarPaciente(paciente1);
        app.cadastrarPaciente(paciente2);

        
        Date hoje = new Date();
        Consulta consulta1 = app.agendarConsulta(paciente1, cirurgiao, hoje);
        consulta1.setDiagnostico("Apendicite aguda - necessária cirurgia");


        Receita receita1 = app.emitirReceita(paciente1, cirurgiao, hoje,
                "Dipirona 1g - 8/8h por 3 dias\n"
                + "Cetoprofeno 100mg - 12/12h por 5 dias\n"
                + "Repouso por 7 dias");

    
        System.out.println("=== SISTEMA HOSPITALAR ===");
        System.out.println("Hospital: " + hospital.getNome());
        
        System.out.println("\nMédicos Cadastrados:");
        for (Unidade unidade : hospital.getUnidades()) {
            for (Medico medico : unidade.getMedicos()) {
                System.out.println("- " + medico.getNome() + 
                    " (" + medico.getEspecialidade().getNome() + ")");
            }
        }

        System.out.println("\nPaciente: " + paciente1.getNome());
        System.out.println("Prontuário: " + paciente1.getNumero());
        System.out.println("Última consulta: " + consulta1.getData());
        System.out.println("Médico: " + consulta1.getMedico().getNome() +
                " (" + consulta1.getMedico().getEspecialidade().getNome() + ")");
        System.out.println("Diagnóstico: " + consulta1.getDiagnostico());
        
        System.out.println("\nReceita médica:");
        System.out.println(receita1.getDescricao());

       
        System.out.println("\nÁreas de Atuação Disponíveis:");
        for (AreaAtuacao area : AreaAtuacao.values()) {
            System.out.println("- " + area.getNome());
        }
    }
}
