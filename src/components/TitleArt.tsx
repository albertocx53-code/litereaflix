// Capa de livro própria da LiteraFlix: tecido colorido, lombada, moldura dourada,
// ornamento em traço fino, título em serifa e o autor ao pé. Nada de imagem de terceiros.
// Se `imageUrl` existir (imagem com direito de uso), ela aparece no lugar da arte.
import type { CSSProperties, ReactNode } from 'react';
import type { Arte as Art } from '@/lib/catalogo';
import { Foto } from './Foto';

type Props = {
  title: string;
  art: Art;
  imageUrl?: string | null;
  variant?: 'poster' | 'wide' | 'fill';
  showText?: boolean;
  className?: string;
  seed?: string;
};

function Ornamento({ kind }: { kind?: string }) {
  let body: ReactNode;
  switch (kind) {
    case 'pena': // pena de escrever
      body = (
        <>
          <path d="M138 30 C96 46 70 90 62 150 C86 120 110 92 150 78 C128 74 116 70 112 64 C126 60 136 52 144 40Z" />
          <path d="M62 150 L52 176" />
          <path d="M70 136 C92 106 112 86 138 70" opacity=".6" />
          <path d="M40 182 C60 178 80 182 100 178" opacity=".5" />
        </>
      );
      break;
    case 'livro': // livro aberto
      body = (
        <>
          <path d="M100 66 C80 56 54 54 34 58 V150 C54 146 80 148 100 158 C120 148 146 146 166 150 V58 C146 54 120 56 100 66Z" />
          <path d="M100 66 V158" />
          {[78, 92, 106, 120].map((y) => <path key={y} d={`M46 ${y} C62 ${y - 3} 78 ${y - 2} 90 ${y + 2} M110 ${y + 2} C122 ${y - 2} 138 ${y - 3} 154 ${y}`} opacity=".55" />)}
        </>
      );
      break;
    case 'flor':
      body = (
        <>
          {Array.from({ length: 8 }, (_, i) => <ellipse key={i} cx="100" cy="74" rx="11" ry="26" transform={`rotate(${i * 45} 100 100)`} />)}
          <circle cx="100" cy="100" r="9" />
          <path d="M100 126 C98 150 102 168 100 190 M100 160 C88 150 76 150 68 156 M100 172 C112 162 124 162 132 168" opacity=".7" />
        </>
      );
      break;
    case 'caravela':
      body = (
        <>
          <path d="M52 132 H148 L134 150 H66Z" />
          <path d="M100 132 V52 M100 56 C120 70 124 96 104 118 M100 62 C80 76 78 100 96 120" />
          <path d="M100 52 L116 46 L100 42" />
          {[160, 172, 184].map((y) => <path key={y} d={`M36 ${y} C50 ${y - 6} 64 ${y + 6} 78 ${y} S106 ${y + 6} 120 ${y} S150 ${y - 6} 164 ${y}`} opacity=".55" />)}
        </>
      );
      break;
    case 'sol':
      body = (
        <>
          <circle cx="100" cy="104" r="26" />
          {Array.from({ length: 16 }, (_, i) => {
            const a = (i / 16) * Math.PI * 2;
            return <path key={i} d={`M${100 + Math.cos(a) * 36} ${104 + Math.sin(a) * 36} L${100 + Math.cos(a) * (i % 2 ? 50 : 60)} ${104 + Math.sin(a) * (i % 2 ? 50 : 60)}`} />;
          })}
        </>
      );
      break;
    case 'lua':
      body = (
        <>
          <path d="M118 52 A52 52 0 1 0 140 148 A44 44 0 1 1 118 52Z" />
          {[[150, 66], [58, 58], [160, 112], [46, 140]].map(([x, y]) => <path key={`${x}${y}`} d={`M${x} ${y - 6} V${y + 6} M${x - 6} ${y} H${x + 6}`} opacity=".7" />)}
        </>
      );
      break;
    case 'barroco': // cartela com volutas
      body = (
        <>
          <path d="M100 46 C130 46 150 62 150 88 C150 116 128 128 100 156 C72 128 50 116 50 88 C50 62 70 46 100 46Z" />
          <path d="M100 66 V136 M78 92 H122" />
          <path d="M50 88 C34 84 30 70 40 62 C48 56 58 62 54 70 M150 88 C166 84 170 70 160 62 C152 56 142 62 146 70" opacity=".7" />
          <path d="M100 156 C96 168 90 174 82 176 M100 156 C104 168 110 174 118 176" opacity=".7" />
        </>
      );
      break;
    case 'louro': // coroa de louros
      body = (
        <>
          <path d="M100 168 C58 160 40 120 52 70 M100 168 C142 160 160 120 148 70" />
          {Array.from({ length: 6 }, (_, i) => {
            const y = 152 - i * 16;
            const xL = 62 - i * 1.5;
            const xR = 138 + i * 1.5;
            return (
              <g key={i}>
                <ellipse cx={xL} cy={y} rx="6" ry="12" transform={`rotate(-40 ${xL} ${y})`} />
                <ellipse cx={xR} cy={y} rx="6" ry="12" transform={`rotate(40 ${xR} ${y})`} />
              </g>
            );
          })}
        </>
      );
      break;
    case 'mascara': // teatro
      body = (
        <>
          <path d="M56 62 C76 56 96 58 110 66 C112 96 104 122 84 132 C66 124 56 100 56 62Z" />
          <path d="M70 84 C74 80 80 80 84 84 M90 86 C94 82 100 82 104 86 M72 108 C80 116 92 116 100 108" />
          <path d="M96 84 C110 74 130 72 148 76 C150 112 140 136 120 146 C108 140 100 128 98 114" opacity=".75" />
          <path d="M112 96 C116 92 122 92 126 96 M130 98 C134 94 140 94 144 98 M114 126 C122 118 134 118 142 126" opacity=".75" />
        </>
      );
      break;
    case 'sertao': // mandacaru e sol
      body = (
        <>
          <circle cx="140" cy="70" r="16" />
          <path d="M92 176 V70 C92 62 104 62 104 70 V176 M92 120 H76 C70 120 68 116 68 110 V90 C68 84 78 84 78 90 V108 H92 M104 132 H120 C126 132 128 128 128 122 V100 C128 94 118 94 118 100 V118 H104" />
          <path d="M30 176 H170" opacity=".7" />
          <path d="M40 186 H160" opacity=".4" />
        </>
      );
      break;
    case 'cidade':
      body = (
        <>
          <path d="M32 176 V118 H58 V96 H82 V130 H96 V70 H124 V112 H142 V88 H168 V176" />
          {[[66, 108], [70, 124], [104, 84], [114, 100], [104, 118], [150, 104], [156, 124], [44, 132], [44, 150]].map(([x, y]) => <rect key={`${x}-${y}`} x={x} y={y} width="6" height="8" opacity=".7" />)}
          <path d="M24 176 H176" />
        </>
      );
      break;
    case 'olho':
      body = (
        <>
          <path d="M34 104 C62 64 138 64 166 104 C138 144 62 144 34 104Z" />
          <circle cx="100" cy="104" r="22" />
          <circle cx="100" cy="104" r="8" fill="currentColor" />
          {[-60, -30, 0, 30, 60].map((d) => <path key={d} d={`M${100 + d * 0.9} ${62 - Math.abs(d) * 0.18} L${100 + d * 1.05} ${50 - Math.abs(d) * 0.22}`} opacity=".6" />)}
        </>
      );
      break;
    case 'estrela':
      body = (
        <>
          <path d="M100 48 L113 88 L156 88 L121 112 L134 152 L100 128 L66 152 L79 112 L44 88 L87 88Z" />
          <circle cx="100" cy="102" r="70" opacity=".35" strokeDasharray="3 7" />
        </>
      );
      break;
    case 'raiz': // árvore e raízes (ancestralidade)
      body = (
        <>
          <path d="M100 176 V108 M100 128 C84 116 70 116 60 104 M100 120 C116 108 130 108 140 96 M100 108 C96 92 88 84 78 78 M100 108 C106 90 116 82 126 76" />
          <circle cx="100" cy="76" r="44" opacity=".55" />
          <path d="M100 176 C88 182 74 182 62 190 M100 176 C112 182 126 182 138 190 M100 176 V194" opacity=".7" />
        </>
      );
      break;
    default: // moldura simples com losango
      body = (
        <>
          <path d="M100 52 L148 104 L100 156 L52 104Z" />
          <path d="M100 74 L126 104 L100 134 L74 104Z" opacity=".6" />
        </>
      );
  }
  return (
    <svg className="art-motif" viewBox="0 0 200 220" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
      {body}
    </svg>
  );
}

export function TitleArt({ title, art, imageUrl, variant = 'poster', showText = true, className = '' }: Props) {
  const style = { '--c1': art.c1, '--c2': art.c2, '--accent': art.accent } as CSSProperties;
  const cls = ['art', variant === 'wide' && 'art--wide', variant === 'fill' && 'art--fill', className].filter(Boolean).join(' ');
  return (
    <div className={cls} style={style} role="img" aria-label={title}>
      <span className="art-lombada" aria-hidden="true" />
      <span className="art-moldura" aria-hidden="true" />
      <Ornamento kind={art.motif} />
      {showText && (
        <div className="art-text" aria-hidden="true">
          {art.kicker && <span className="art-kicker">{art.kicker}</span>}
          <span className={`art-title${title.length > 24 || title.split(' ').some((w) => w.length > 11) ? ' art-title--longo' : ''}`}>{title}</span>
          {art.autor && <span className="art-autor">{art.autor}</span>}
          <span className="art-selo">LF</span>
        </div>
      )}
      {imageUrl && <Foto src={imageUrl} kicker={art.kicker} titulo={title} autor={art.autor} comTexto={showText} />}
    </div>
  );
}
