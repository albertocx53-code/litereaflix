'use client';

import { useEffect, useState, type CSSProperties } from 'react';

// Faixas de luz da "entrada na marca". Semente fixa: servidor e navegador geram o mesmo HTML.
function faixas() {
  let s = 1922;
  const r = () => ((s = (s * 16807) % 2147483647) - 1) / 2147483646;
  const cores = ['#e3b45a', '#f6d48c', '#b8862f', '#7a1f2b', '#a3283a', '#fff1cf'];
  return Array.from({ length: 46 }, (_, i) => ({
    '--x': `${((i - 23) * 2.2 + (r() - 0.5) * 1.4).toFixed(2)}vw`,
    '--w': `${(0.35 + r() * 1.5).toFixed(2)}vw`,
    '--c': cores[Math.floor(r() * cores.length)],
    '--d': `${(r() * 0.35).toFixed(2)}s`,
    '--o': (0.45 + r() * 0.55).toFixed(2),
  }) as CSSProperties);
}
const FAIXAS = faixas();

/**
 * Abertura estilo vinheta de cinema (uns 4 s): tela preta, o nome LiteraFlix
 * surge com impacto, um brilho dourado atravessa as letras e a câmera mergulha
 * na marca, que se desfaz em faixas de luz até revelar o site.
 */
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
    const t = setTimeout(fim, 4100);
    const tecla = (e: KeyboardEvent) => { if (e.key === 'Escape' || e.key === 'Enter' || e.key === ' ') fim(); };
    document.addEventListener('keydown', tecla);
    (window as unknown as { __pularAbertura?: () => void }).__pularAbertura = fim;
    return () => { clearTimeout(t); document.removeEventListener('keydown', tecla); };
  }, []);

  if (!viva) return null;
  return (
    <div id="abertura" className="abertura" aria-hidden="true" onClick={() => (window as unknown as { __pularAbertura?: () => void }).__pularAbertura?.()}>
      <div className="ab-halo" />
      <div className="ab-faixas">{FAIXAS.map((st, i) => <i key={i} style={st} />)}</div>
      <div className="ab-camera">
        <div className="ab-marca">
          <span className="ab-a">Litera</span><span className="ab-b">flix</span>
        </div>
        <div className="ab-reflexo" />
      </div>
      <div className="ab-flash" />
      <div className="ab-grao" />
      <span className="ab-pular">Clique para pular</span>
    </div>
  );
}
