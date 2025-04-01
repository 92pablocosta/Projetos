package br.com.programweb.sorteioviga.usuario;

import br.com.programweb.sorteioviga.bilhete.Bilhete;
import jakarta.persistence.*;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import lombok.*;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
@Builder
@Entity
@Table(name = "tb_usuario")
public class Usuario {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @NotBlank(message = "O nome não pode estar vazio.")
    private String nome;

    @Email(message = "E-mail deve ser válido.")
    @NotBlank(message = "O e-mail não pode estar vazio.")
    private String email;

    private LocalDate dataNascimento;

    @Column(length = 14)
    private String cpf;

    private String telefone;

    @OneToMany(mappedBy = "usuario", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Bilhete> bilhetes = new ArrayList<>();

    public void adicionarBilhete(Bilhete bilhete) {
        bilhetes.add(bilhete);
        bilhete.setUsuario(this);
    }

    public void removerBilhete(Bilhete bilhete) {
        bilhetes.remove(bilhete);
        bilhete.setUsuario(null);
    }
}
