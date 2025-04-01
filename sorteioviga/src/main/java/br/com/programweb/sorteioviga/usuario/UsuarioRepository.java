package br.com.programweb.sorteioviga.usuario;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * Interface responsável pela persistência (CRUD) da entidade Usuario.
 *
 * O Spring Data JPA gera automaticamente as implementações de métodos básicos
 * (findAll, findById, save, deleteById, etc.) a partir de JpaRepository.
 */
@Repository
public interface UsuarioRepository extends JpaRepository<Usuario, Long> {

    /**
     * Retorna true se existir algum usuário com o e-mail fornecido.
     */
    boolean existsByEmail(String email);

    /**
     * Retorna true se existir algum usuário com o CPF fornecido.
     */
    boolean existsByCpf(String cpf);
}
