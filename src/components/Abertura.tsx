'use client';

import { useEffect, useState, type CSSProperties } from 'react';

// Letras que sobem do livro aberto. Semente fixa: servidor e navegador geram o mesmo HTML.
function letrasSoltas() {
  let s = 1922;
  const r = () => ((s = (s * 16807) % 2147483647) - 1) / 2147483646;
  const pool = 'aeiouçãéêíóõúbcdfglmnprstvALFP&?!«»';
  return Array.from({ length: 34 }, () => ({
    ch: pool[Math.floor(r() * pool.length)],
    st: {
      '--x': `${((r() * 2 - 1) * 46).toFixed(1)}vw`,
      '--y': `${(-30 - r() * 45).toFixed(1)}vh`,
      '--r': `${((r() * 2 - 1) * 70).toFixed(0)}deg`,
      '--s': (0.7 + r() * 1.6).toFixed(2),
      '--t': `${(0.9 + r() * 0.9).toFixed(2)}s`,
    } as CSSProperties,
  }));
}
const SOLTAS = letrasSoltas();
const MARCA = 'LiteraFlix'.split('');

/** Abertura: um livro se abre, as letras escapam das páginas e o nome se escreve em dourado. */
export function Abertura() {
  const [viva, setViva] = useState(true);

  useEffect(() => {
    const raiz = document.documentElement;
    if (!raiz.classList.contains('com-abertura')) { setViva(false); return; }
    const fim = () => {
      raiz.classList.remove('com-abertura');
      raiz.classList.add('abertura-fim');
      setViva(false);
    };
    const t = setTimeout(fim, 4000);
    const tecla = (e: KeyboardEvent) => { if (e.key === 'Escape' || e.key === 'Enter' || e.key === ' ') fim(); };
    document.addEventListener('keydown', tecla);
    (window as unknown as { __pularAbertura?: () => void }).__pularAbertura = fim;
    return () => { clearTimeout(t); document.removeEventListener('keydown', tecla); };
  }, []);

  if (!viva) return null;
  return (
    <div id="abertura" className="abertura" aria-hidden="true" onClick={() => (window as unknown as { __pularAbertura?: () => void }).__pularAbertura?.()}>
      <div className="ab-luz" />
      <div className="ab-livro">
        <span className="ab-pagina ab-pagina--e" />
        <span className="ab-pagina ab-pagina--d" />
        <span className="ab-capa ab-capa--e" />
        <span className="ab-capa ab-capa--d" />
      </div>
      <div className="ab-soltas">{SOLTAS.map((l, i) => <i key={i} style={l.st}>{l.ch}</i>)}</div>
      <div className="ab-palco">
        <div className="ab-marca">
          {MARCA.map((l, i) => <span key={i} className={i >= 6 ? 'ouro' : undefined} style={{ '--i': String(i) } as CSSProperties}>{l}</span>)}
        </div>
        <svg className="ab-traco" viewBox="0 0 600 40" fill="none" aria-hidden="true"><path d="M10 26 C120 6 220 36 320 20 S500 8 590 18" /></svg>
        <p className="ab-slogan">Literatura que vira aula</p>
      </div>
      <span className="ab-pular">Clique para pular</span>
    </div>
  );
}
