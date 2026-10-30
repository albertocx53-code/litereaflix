'use client';

import { useEffect, useRef, useState } from 'react';

type Props = { src: string; kicker?: string; titulo?: string; autor?: string; comTexto?: boolean };

/**
 * Imagem por cima da capa desenhada. Se a imagem não carregar (link quebrado,
 * sem internet), ela some e a capa desenhada que está por baixo aparece.
 */
export function Foto({ src, kicker, titulo, autor, comTexto = true }: Props) {
  const img = useRef<HTMLImageElement>(null);
  const [ok, setOk] = useState(true);

  useEffect(() => {
    const i = img.current;
    if (i && i.complete && i.naturalWidth === 0) setOk(false);
  }, []);

  if (!ok) return null;
  return (
    <span className="art-foto">
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img ref={img} src={src} alt="" loading="lazy" decoding="async" referrerPolicy="no-referrer" onError={() => setOk(false)} />
      {comTexto && (
        <span className="art-foto-txt" aria-hidden="true">
          {kicker && <span className="art-kicker">{kicker}</span>}
          {titulo && <span className={`art-title${titulo.length > 24 || titulo.split(' ').some((w) => w.length > 11) ? ' art-title--longo' : ''}`}>{titulo}</span>}
          {autor && <span className="art-autor">{autor}</span>}
        </span>
      )}
    </span>
  );
}
