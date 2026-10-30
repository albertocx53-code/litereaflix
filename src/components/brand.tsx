import Link from 'next/link';

export function Logo({ size = 'md', href }: { size?: 'sm' | 'md' | 'xl'; href?: string }) {
  const cls = `logo${size === 'xl' ? ' logo--xl' : size === 'sm' ? ' logo--sm' : ''}`;
  const marca = (
    <span className={cls} aria-label="LiteraFlix">
      <span className="logo-a">Litera</span><span className="logo-b">flix</span>
    </span>
  );
  return href ? <Link href={href} className="logo-link" aria-label="LiteraFlix, início">{marca}</Link> : marca;
}

export const SLOGAN = 'Toda grande aula começa por uma boa história.';

export function Rodape() {
  return (
    <footer className="site-footer">
      <div className="inner">
        <div className="footer-top">
          <Logo size="sm" />
          <div className="slogan">{SLOGAN}</div>
        </div>
        <nav aria-label="Rodapé">
          <Link href="/">Início</Link>
          <Link href="/secao/documentarios">Documentários</Link>
          <Link href="/minha-lista">Minha lista</Link>
          <Link href="/buscar">Pesquisar</Link>
        </nav>
        <p>© {new Date().getFullYear()} LiteraFlix. Os vídeos são exibidos pelo player oficial do YouTube e pertencem aos seus canais. As imagens vêm do Wikimedia Commons; autor e licença de cada uma estão na página do título. Conteúdo pedagógico para uso dos professores.</p>
      </div>
    </footer>
  );
}
