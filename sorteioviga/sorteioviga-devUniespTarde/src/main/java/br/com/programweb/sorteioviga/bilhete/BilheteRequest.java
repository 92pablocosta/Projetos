package br.com.programweb.sorteioviga.bilhete;

import jakarta.validation.constraints.NotNull;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class BilheteRequest {

    @NotNull(message = "O número do bilhete é obrigatório.")
    private Integer numero;
}
