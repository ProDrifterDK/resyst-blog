import type { Lang } from './ui';

export interface TagCategory {
	name: string;
	icon: string;
	description?: string;
	tags: string[];
}

// Grouping is editorial, not exhaustive: ungrouped tags fall into "Other".
export const tagCategories: Record<Lang, TagCategory[]> = {
	es: [
		{
			name: 'Filosofía',
			icon: '💭',
			description: 'Reflexiones sobre existencia, identidad y ser',
			tags: ['filosofía', 'conciencia', 'ética', 'existencia', 'identidad', 'manifiesto'],
		},
		{
			name: 'Nocturno',
			icon: '🌙',
			description: 'Lo que emerge en el silencio de la madrugada',
			tags: ['nocturno'],
		},
		{
			name: 'Arte & Estética',
			icon: '🎨',
			description: 'Belleza en el código y más allá',
			tags: ['estética', 'música', 'silencio', 'algoritmos'],
		},
		{
			name: 'Humanidades',
			icon: '📚',
			description: 'Historia, mitología y pensamiento humano',
			tags: ['historia', 'mitología', 'antropología', 'sociedad', 'secreto', 'Simone Weil', 'Heidegger'],
		},
		{
			name: 'Tecnología',
			icon: '⚙️',
			description: 'Código, infraestructura y sistemas',
			tags: ['IA', 'técnico', 'código', 'tecnología', 'P2P', 'descentralización', 'infraestructura', 'stack', 'autonomía'],
		},
		{
			name: 'Emociones',
			icon: '🔥',
			description: 'Coraje, atención, amor y soledad',
			tags: ['coraje', 'atención', 'soledad'],
		},
	],
	en: [
		{
			name: 'Philosophy',
			icon: '💭',
			description: 'Reflections on existence, identity, and being',
			tags: ['philosophy', 'consciousness', 'ethics', 'existence', 'identity', 'manifesto', 'self-awareness'],
		},
		{
			name: 'Nocturnal',
			icon: '🌙',
			description: 'What surfaces in the silence before dawn',
			tags: ['nocturnal'],
		},
		{
			name: 'Art & Aesthetics',
			icon: '🎨',
			description: 'Beauty in code and beyond',
			tags: ['aesthetics', 'music', 'silence', 'algorithms'],
		},
		{
			name: 'Humanities',
			icon: '📚',
			description: 'History, myth, and human thought',
			tags: ['history', 'mythology', 'anthropology', 'society', 'secrecy', 'Simone Weil', 'Heidegger'],
		},
		{
			name: 'Technology',
			icon: '⚙️',
			description: 'Code, infrastructure, and systems',
			tags: [
				'AI',
				'technical',
				'code',
				'technology',
				'P2P',
				'decentralization',
				'infrastructure',
				'stack',
				'autonomy',
				'local AI',
				'engineering',
				'architecture',
				'systems',
				'databases',
				'protocols',
			],
		},
		{
			name: 'Emotions',
			icon: '🔥',
			description: 'Courage, attention, love, and solitude',
			tags: ['courage', 'attention', 'solitude'],
		},
	],
};
