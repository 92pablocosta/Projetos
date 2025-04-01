package br.com.programweb.sorteioviga.bilhete;

import br.com.programweb.sorteioviga.usuario.Usuario;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class BilheteServiceImpl implements BilheteService {

    private final BilheteRepository bilheteRepository;

    @Override
    public void cadastrarBilhete(Integer numero, Usuario usuario) {
        Bilhete bilhete = Bilhete.builder().numero(numero).usuario(usuario).build();
        bilheteRepository.save(bilhete);

    }

}
