import { defaultLang, languages, ui, type Lang, type UIKey } from './ui';

export { defaultLang, languages, ui, type Lang, type UIKey };

/** Locale implied by the current URL: /en/... is English, everything else is Spanish. */
export function getLangFromUrl(url: URL): Lang {
	const [, first] = url.pathname.split('/');
	if (first && first in languages) return first as Lang;
	return defaultLang;
}

/** Translator bound to one locale. */
export function useTranslations(lang: Lang) {
	return function t(key: UIKey): string {
		return ui[lang][key] ?? ui[defaultLang][key];
	};
}

/**
 * Prefix an already-localized path for the target locale.
 * Spanish lives at the root, English under /en.
 */
export function localizePath(path: string, lang: Lang): string {
	const clean = path.startsWith('/') ? path : `/${path}`;
	if (lang === defaultLang) return clean;
	return clean === '/' ? '/en/' : `/en${clean}`;
}

/**
 * Counterpart path for the other locale. Tag detail pages collapse to the
 * tag index because tag vocabularies differ between languages; post pages
 * need the explicit mapping supplied by the caller.
 */
export function otherLangPath(pathname: string, lang: Lang): string {
	const base = pathname.replace(/^\/en(?=\/|$)/, '') || '/';
	const isTagDetail = /^\/(?:en\/)?blog\/tags\/[^/]+\/?$/.test(pathname);
	if (isTagDetail) return localizePath('/blog/tags/', lang === 'es' ? 'en' : 'es');
	return localizePath(base, lang === 'es' ? 'en' : 'es');
}

/** True when the given locale is the one currently rendered. */
export function isLang(lang: Lang, candidate: string): boolean {
	return lang === candidate;
}
