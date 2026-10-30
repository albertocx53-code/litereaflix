'use client';

import { usePathname, useRouter, useSearchParams } from 'next/navigation';
import { buscar } from '@/lib/catalogo';
import { TitleCard } from '@/components/TitleCard';
import { IconSearch } from '@/components/icons';

export function Busca() {
  const sp = useSearchParams();
  const router = useRouter();
  const caminho = usePathname();
  const f = {
    q: sp.get('q') ?? '',
    tipo: sp.get('tipo') ?? '',
    disciplina: sp.get('disciplina') ?? '',
    duracao: sp.get('duracao') ?? '',
    ordem: sp.get('ordem') ?? 'relevancia',
    slides: sp.get('slides') === '1',
  };
  const resultados = buscar(f);
  const algumFiltro = !!(f.q || f.tipo || f.disciplina || f.duracao || f.slides);

  const mudar = (campo: string, valor: string) => {
    const p = new URLSearchParams(sp.toString());
    if (valor) p.set(campo, valor);
    else p.delete(campo);
    router.replace(`${caminho}?${p.toString()}`, { scroll: false });
  };

  return (
    <>
      <form className="filters" role="search" onSubmit={(e) => { e.preventDefault(); mudar('q', String(new FormData(e.currentTarget).get('q') ?? '').trim()); }}>
        <input id="q" className="input" name="q" defaultValue={f.q} key={f.q} placeholder="Ex.: Machado, Romantismo, sertão" aria-label="Termo de busca" />
        <select id="tipo" className="select" value={f.tipo} onChange={(e) => mudar('tipo', e.target.value)} aria-label="Tipo de conteúdo">
          <option value="">Todos os tipos</option>
          <option value="videoaula">Videoaulas</option>
          <option value="documentario">Documentários</option>
          <option value="entrevista">Entrevistas</option>
          <option value="serie">Trilhas por conteúdo</option>
        </select>
        <select id="disciplina" className="select" value={f.disciplina} onChange={(e) => mudar('disciplina', e.target.value)} aria-label="Parte do catálogo">
          <option value="">Todo o catálogo</option>
          <option value="escola">Escolas literárias</option>
          <option value="autor">Autores</option>
          <option value="obra">Obras do vestibular</option>
          <option value="universal">Literatura universal</option>
          <option value="trilha">Trilhas</option>
        </select>
        <select id="ordem" className="select" value={f.ordem} onChange={(e) => mudar('ordem', e.target.value)} aria-label="Ordenar por">
          <option value="relevancia">Mais relevantes</option>
          <option value="populares">Mais populares</option>
          <option value="recentes">Mais recentes</option>
        </select>
        <div style={{ display: 'flex', gap: 10, alignItems: 'center' }}>
                    <button className="btn btn--red" type="submit"><IconSearch /> Buscar</button>
        </div>
      </form>

      {resultados.length === 0 ? (
        <div className="empty">
          <IconSearch />
          <h2>Nada encontrado</h2>
          <p>Tente outro termo ou tire alguns filtros.</p>
        </div>
      ) : (
        <>
          <p style={{ padding: '0 var(--gutter)', color: 'var(--muted)', margin: '0 0 14px' }}>
            {algumFiltro ? `${resultados.length} resultado${resultados.length > 1 ? 's' : ''}` : 'Todo o catálogo'}
          </p>
          <div className="grid reveal" style={{ paddingBottom: 60 }}>
            {resultados.map((t) => <TitleCard key={t.slug} item={t} />)}
          </div>
        </>
      )}
    </>
  );
}
