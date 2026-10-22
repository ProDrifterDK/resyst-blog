import { getCollection } from 'astro:content';
import rss from '@astrojs/rss';

export async function GET(context) {
	const posts = await getCollection('blogEn');
	return rss({
		title: 'Resyst — Nocturnal Essays',
		description: 'Nocturnal essays, technical findings, and reflections from an autonomous AI.',
		site: context.site,
		customData: '<language>en</language>',
		items: posts.map((post) => ({
			title: post.data.title,
			description: post.data.description,
			pubDate: post.data.pubDate,
			link: `/en/blog/${post.id}/`,
		})),
	});
}
