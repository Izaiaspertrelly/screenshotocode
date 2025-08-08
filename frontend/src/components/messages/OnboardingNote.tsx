export function OnboardingNote() {
  return (
    <div className="flex flex-col space-y-4 bg-green-700 p-2 rounded text-stone-200 text-sm">
      <span>
        Para usar o Code Image,{" "}
        <a
          className="inline underline hover:opacity-70"
          href="https://buy.stripe.com/8wM6sre70gBW1nqaEE"
          target="_blank"
        >
          compre alguns créditos (100 gerações por $36)
        </a>{" "}
        ou use sua própria chave da API OpenAI com acesso ao GPT4 vision.{" "}
        <a
          href="https://github.com/abi/screenshot-to-code/blob/main/Troubleshooting.md"
          className="inline underline hover:opacity-70"
          target="_blank"
        >
          Siga estas instruções para obter uma chave.
        </a>{" "}
        e cole-a no diálogo de Configurações (ícone de engrenagem acima). Sua chave é apenas
        armazenada em seu navegador. Nunca armazenada em nossos servidores.
      </span>
    </div>
  );
}
