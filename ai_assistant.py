"""
Assistant IA pour l'interprétation des résultats
Utilise OpenAI GPT pour générer des interprétations détaillées
"""

import openai
import os
from dotenv import load_dotenv
from real_world_ai_interpreter import RealWorldAIInterpreter

load_dotenv()

class AIAssistant:
    def __init__(self):
        """Initialise l'assistant IA"""
        self.api_key = os.getenv('OPENAI_API_KEY', '')
        if self.api_key:
            openai.api_key = self.api_key
        self.real_world_interpreter = RealWorldAIInterpreter()
    
    def interpret_results(self, analysis_results, is_premium=False, platform_comparison=None):
        """
        Interprète les résultats d'analyse
        
        Parameters:
        analysis_results (dict): Résultats des tests statistiques
        is_premium (bool): Si l'utilisateur est premium
        platform_comparison (DataFrame): Comparaison des plateformes
        """
        if not self.api_key:
            return self._fallback_interpretation(analysis_results, is_premium, platform_comparison)
        
        try:
            # Préparer le contexte
            context = self._prepare_context(analysis_results, platform_comparison)
            
            if is_premium:
                prompt = self._create_premium_prompt(context)
            else:
                prompt = self._create_basic_prompt(context)
            
            # Appel à l'API OpenAI
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Vous êtes un expert en analyse de données des réseaux sociaux. Vous aidez les utilisateurs à comprendre leurs métriques d'engagement."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=800 if is_premium else 300,
                temperature=0.7
            )
            
            return response.choices[0].message.content
        
        except Exception as e:
            return self._fallback_interpretation(analysis_results, is_premium, platform_comparison)
    
    def _prepare_context(self, analysis_results, platform_comparison):
        """Prépare le contexte pour l'IA"""
        context = "Résultats d'analyse:\n\n"
        
        for test_name, result in analysis_results.items():
            if test_name == 'kruskal_wallis':
                context += f"Test de Kruskal-Wallis: p-value = {result['p_value']:.4f}, "
                context += f"significatif = {result['significant']}\n"
            
            elif test_name == 'spearman':
                context += f"Corrélation de Spearman: r = {result['correlation']:.3f}, "
                context += f"p-value = {result['p_value']:.4f}\n"
            
            elif test_name == 'chi2':
                context += f"Test du Chi-carré: χ² = {result['chi2_statistic']:.2f}, "
                context += f"p-value = {result['p_value']:.4f}\n"
            
            elif test_name == 'prediction':
                context += f"Modèle de prédiction: R² = {result['r2_score']:.3f}, "
                context += f"RMSE = {result['rmse']:.2f}\n"
            
            elif test_name.startswith('prediction_'):
                target_name = result.get('target') or test_name.split('prediction_', 1)[-1]
                context += f"Prédiction de {target_name}: R² = {result['r2_score']:.3f}, "
                context += f"RMSE = {result['rmse']:.2f}\n"
        
        if platform_comparison is not None:
            context += "\nComparaison des plateformes:\n"
            for _, row in platform_comparison.iterrows():
                context += f"{row['platform']}: engagement moyen = {row['mean_engagement']:.2f}%\n"
        
        return context
    
    def _create_basic_prompt(self, context):
        """Crée un prompt pour les utilisateurs gratuits"""
        return f"""
Voici les résultats d'une analyse de données de réseaux sociaux:

{context}

Donnez une interprétation COURTE et SIMPLE de ces résultats (maximum 3-4 phrases).
Concentrez-vous sur les points les plus importants pour un débutant.
"""
    
    def _create_premium_prompt(self, context):
        """Crée un prompt détaillé pour les utilisateurs premium"""
        return f"""
Vous êtes un expert en marketing digital et analyse de données des réseaux sociaux. Analysez ces résultats et fournissez une interprétation PROFESSIONNELLE et ACTIONNABLE.

{context}

Fournissez une analyse COMPLÈTE et DÉTAILLÉE incluant:

🎯 **ANALYSE STATISTIQUE APPROFONDIE:**
- Explication technique des résultats (significativité, effect size, puissance)
- Interprétation des valeurs critiques et seuils de confiance
- Analyse des distributions et patterns détectés

📊 **INSIGHTS STRATÉGIQUES CONCRETS:**
- Recommandations spécifiques par plateforme avec exemples concrets
- Stratégies de contenu basées sur les données (types de posts, timing, formats)
- Optimisations d'audience et de ciblage
- Tactiques d'engagement spécifiques

🚀 **PLAN D'ACTION OPÉRATIONNEL:**
- Actions immédiates à mettre en place (cette semaine)
- Objectifs quantifiés et KPIs à suivre
- Tests A/B à réaliser avec hypothèses précises
- Timeline de mise en œuvre (court/moyen/long terme)

💡 **BENCHMARKING ET COMPÉTITION:**
- Comparaison avec les standards du secteur
- Opportunités de différenciation identifiées
- Menaces et risques à surveiller

📈 **PRÉDICTIONS ET TENDANCES:**
- Projections basées sur les données actuelles
- Tendances saisonnières ou cycliques détectées
- Facteurs externes à considérer

Soyez PRÉCIS, TECHNIQUE mais ACCESSIBLE. Utilisez des exemples concrets, des chiffres spécifiques et des recommandations actionables. Visez 20-25 phrases structurées avec des emojis pour la lisibilité.
"""
    
    def _fallback_interpretation(self, analysis_results, is_premium, platform_comparison):
        """Interprétation de secours sans API OpenAI - Version améliorée"""
        interpretation = "📊 **ANALYSE APPROFONDIE DES RÉSULTATS**\n\n"
        
        # Interprétations détaillées des tests
        for test_name, result in analysis_results.items():
            if test_name == 'kruskal_wallis' and 'interpretation' in result:
                interpretation += f"🔍 **Test de Kruskal-Wallis:**\n"
                interpretation += f"• {result['interpretation']}\n"
                if result.get('significant', False):
                    interpretation += f"• **Impact:** Différence significative détectée entre les groupes (p={result.get('p_value', 0):.4f})\n"
                    interpretation += f"• **Action:** Concentrez-vous sur le groupe le plus performant et analysez ses caractéristiques\n"
                else:
                    interpretation += f"• **Impact:** Pas de différence significative entre les groupes\n"
                    interpretation += f"• **Action:** Augmentez la taille d'échantillon ou testez d'autres variables\n"
                interpretation += "\n"
            
            elif test_name == 'spearman' and 'interpretation' in result:
                interpretation += f"📈 **Corrélation de Spearman:**\n"
                interpretation += f"• {result['interpretation']}\n"
                corr = result.get('correlation', 0)
                if abs(corr) > 0.7:
                    interpretation += f"• **Impact:** Corrélation forte (r={corr:.3f}) - Relation très prévisible\n"
                    interpretation += f"• **Action:** Exploitez cette relation pour optimiser vos posts\n"
                elif abs(corr) > 0.3:
                    interpretation += f"• **Impact:** Corrélation modérée (r={corr:.3f}) - Relation partiellement prévisible\n"
                    interpretation += f"• **Action:** Testez cette relation avec différents types de contenu\n"
                else:
                    interpretation += f"• **Impact:** Corrélation faible (r={corr:.3f}) - Relation peu prévisible\n"
                    interpretation += f"• **Action:** Cherchez d'autres facteurs explicatifs\n"
                interpretation += "\n"
            
            elif test_name == 'chi2' and 'interpretation' in result:
                interpretation += f"📊 **Test du Chi-carré:**\n"
                interpretation += f"• {result['interpretation']}\n"
                if result.get('significant', False):
                    interpretation += f"• **Impact:** Association significative détectée (χ²={result.get('chi2_statistic', 0):.2f})\n"
                    interpretation += f"• **Action:** Analysez les catégories les plus performantes\n"
                else:
                    interpretation += f"• **Impact:** Pas d'association significative\n"
                    interpretation += f"• **Action:** Testez d'autres variables catégorielles\n"
                interpretation += "\n"
            
            elif test_name.startswith('prediction') and 'interpretation' in result:
                target_name = result.get('target') or test_name.split('prediction_', 1)[-1] or 'métrique'
                target_pretty = target_name.replace('_', ' ').title()
                is_addiction = 'addict' in target_name.lower()
                icon = "🧠" if is_addiction else "🔮"
                
                interpretation += f"{icon} **Modèle de Prédiction ({target_pretty}):**\n"
                interpretation += f"• {result['interpretation']}\n"
                r2 = result.get('r2_score', 0)
                
                if r2 > 0.7:
                    interpretation += f"• **Impact:** Modèle très fiable (R²={r2:.3f}) - Prédictions précises\n"
                    if is_addiction:
                        interpretation += f"• **Action:** Détectez les profils à haut risque et proposez un accompagnement avant qu'ils ne décrochent.\n"
                    else:
                        interpretation += f"• **Action:** Utilisez ce modèle pour planifier votre contenu\n"
                elif r2 > 0.5:
                    interpretation += f"• **Impact:** Modèle modérément fiable (R²={r2:.3f}) - Prédictions acceptables\n"
                    interpretation += f"• **Action:** Améliorez le modèle avec plus de données\n"
                else:
                    interpretation += f"• **Impact:** Modèle peu fiable (R²={r2:.3f}) - Prédictions imprécises\n"
                    interpretation += f"• **Action:** Collectez plus de données ou testez d'autres variables\n"
                
                if is_addiction:
                    interpretation += "• **Alerte:** Combinez ces scores avec les heures de sommeil et la santé mentale pour prioriser les interventions.\n"
                
                interpretation += "\n"
        
        # Comparaison des plateformes avec analyse détaillée
        if platform_comparison is not None and len(platform_comparison) > 0:
            interpretation += f"🏆 **ANALYSE COMPARATIVE DES PLATEFORMES:**\n"
            
            # Calculer les statistiques
            mean_eng = platform_comparison['mean_engagement'].mean()
            std_eng = platform_comparison['mean_engagement'].std()
            best_platform = platform_comparison.loc[platform_comparison['mean_engagement'].idxmax()]
            worst_platform = platform_comparison.loc[platform_comparison['mean_engagement'].idxmin()]
            
            interpretation += f"• **Performance moyenne:** {mean_eng:.2f}% (±{std_eng:.2f}%)\n"
            interpretation += f"• **Meilleure plateforme:** {best_platform['platform']} ({best_platform['mean_engagement']:.2f}%)\n"
            interpretation += f"• **Plateforme à améliorer:** {worst_platform['platform']} ({worst_platform['mean_engagement']:.2f}%)\n\n"
            
            # Recommandations spécifiques par plateforme
            interpretation += f"💡 **RECOMMANDATIONS PAR PLATEFORME:**\n"
            for _, row in platform_comparison.iterrows():
                platform = row['platform']
                engagement = row['mean_engagement']
                
                if engagement > mean_eng * 1.2:
                    interpretation += f"✅ **{platform}:** Excellente performance! Continuez cette stratégie et analysez les éléments de succès.\n"
                elif engagement > mean_eng * 0.8:
                    interpretation += f"⚖️ **{platform}:** Performance correcte. Optimisez le timing et testez de nouveaux formats.\n"
                else:
                    interpretation += f"⚠️ **{platform}:** Performance à améliorer. Revoyez votre stratégie de contenu et votre audience.\n"
            
            interpretation += "\n"
        
        # Ajout d'insights premium détaillés
        if is_premium:
            interpretation += self._add_premium_insights(analysis_results, platform_comparison)
        else:
            interpretation += "\n✨ **Passez en Premium pour des insights détaillés et des recommandations personnalisées!**"
        
        return interpretation
    
    def _add_premium_insights(self, analysis_results, platform_comparison):
        """Ajoute des insights premium détaillés et concrets"""
        insights = "🚀 **PLAN D'ACTION PREMIUM DÉTAILLÉ**\n\n"
        
        # 1. ANALYSE DES CORRÉLATIONS AVEC RECOMMANDATIONS CONCRÈTES
        if 'spearman' in analysis_results:
            corr = analysis_results['spearman']['correlation']
            insights += f"📈 **EXPLOITATION DES CORRÉLATIONS:**\n"
            
            if abs(corr) > 0.7:
                insights += f"• **Corrélation forte détectée (r={corr:.3f})** - Opportunité majeure!\n"
                insights += f"• **Action immédiate:** Augmentez la variable prédictive de 20-30% sur vos prochains posts\n"
                insights += f"• **Test A/B:** Comparez 10 posts avec optimisation vs 10 posts normaux\n"
                insights += f"• **Timeline:** Résultats attendus dans 2-3 semaines\n"
            elif abs(corr) > 0.3:
                insights += f"• **Corrélation modérée (r={corr:.3f})** - Potentiel à exploiter\n"
                insights += f"• **Action immédiate:** Testez cette relation sur 3 plateformes différentes\n"
                insights += f"• **Optimisation:** Augmentez progressivement (10%, 20%, 30%)\n"
                insights += f"• **Monitoring:** Suivez l'évolution sur 1 mois\n"
            else:
                insights += f"• **Corrélation faible (r={corr:.3f})** - Facteurs cachés à découvrir\n"
                insights += f"• **Action immédiate:** Analysez le contenu qualitatif (hashtags, timing, format)\n"
                insights += f"• **Recherche:** Testez 5 nouvelles variables non mesurées\n"
                insights += f"• **Focus:** Concentrez-vous sur l'engagement émotionnel\n"
            insights += "\n"
        
        # 2. STRATÉGIES PAR PLATEFORME AVEC EXEMPLES CONCRETS
        if platform_comparison is not None and len(platform_comparison) > 0:
            insights += f"🎯 **STRATÉGIES SPÉCIFIQUES PAR PLATEFORME:**\n"
            
            for _, row in platform_comparison.iterrows():
                platform = row['platform']
                engagement = row['mean_engagement']
                mean_eng = platform_comparison['mean_engagement'].mean()
                
                if platform.lower() == 'tiktok':
                    if engagement > mean_eng * 1.2:
                        insights += f"✅ **TikTok - Excellente performance ({engagement:.2f}%):**\n"
                        insights += f"• Continuez les vidéos de 15-30 secondes avec des transitions rapides\n"
                        insights += f"• Utilisez les trending sounds (Top 10 du jour)\n"
                        insights += f"• Postez entre 18h-21h (pic d'engagement)\n"
                        insights += f"• Testez 3 nouveaux formats: transitions, tutos, challenges\n"
                    else:
                        insights += f"⚠️ **TikTok - À améliorer ({engagement:.2f}%):**\n"
                        insights += f"• Revoyez votre stratégie: vidéos trop longues ou timing incorrect\n"
                        insights += f"• Testez les trending hashtags (#fyp, #viral)\n"
                        insights += f"• Optimisez les 3 premières secondes (hook fort)\n"
                        insights += f"• Analysez vos top 5 vidéos et répliquez le format\n"
                
                elif platform.lower() == 'instagram':
                    if engagement > mean_eng * 1.2:
                        insights += f"✅ **Instagram - Excellente performance ({engagement:.2f}%):**\n"
                        insights += f"• Alternez Reels (70%) et Stories (30%)\n"
                        insights += f"• Utilisez 20-30 hashtags pertinents par post\n"
                        insights += f"• Postez à 11h et 19h (meilleurs créneaux)\n"
                        insights += f"• Testez les carrousels avec 5-7 images\n"
                    else:
                        insights += f"⚠️ **Instagram - À améliorer ({engagement:.2f}%):**\n"
                        insights += f"• Augmentez la fréquence: 1 post/jour minimum\n"
                        insights += f"• Optimisez les Stories avec stickers interactifs\n"
                        insights += f"• Testez les IGTV pour du contenu long\n"
                        insights += f"• Utilisez les hashtags de niche (moins compétitifs)\n"
                
                elif platform.lower() == 'facebook':
                    if engagement > mean_eng * 1.2:
                        insights += f"✅ **Facebook - Excellente performance ({engagement:.2f}%):**\n"
                        insights += f"• Partagez du contenu vidéo natif (pas de liens externes)\n"
                        insights += f"• Posez des questions pour générer des commentaires\n"
                        insights += f"• Postez en début d'après-midi (13h-15h)\n"
                        insights += f"• Utilisez les groupes Facebook pour amplifier\n"
                    else:
                        insights += f"⚠️ **Facebook - À améliorer ({engagement:.2f}%):**\n"
                        insights += f"• Évitez les liens externes (algorithme pénalise)\n"
                        insights += f"• Créez du contenu local et communautaire\n"
                        insights += f"• Testez les Facebook Live (engagement élevé)\n"
                        insights += f"• Optimisez pour les partages (contenu viral)\n"
                
                insights += "\n"
        
        # 3. RECOMMANDATIONS BASÉES SUR LA PRÉDICTION
        prediction_keys = [k for k in analysis_results if k.startswith('prediction')]
        if prediction_keys:
            for key in prediction_keys:
                result = analysis_results[key]
                target_name = result.get('target') or key.split('prediction_', 1)[-1] or 'métrique'
                target_pretty = target_name.replace('_', ' ').title()
                r2 = result.get('r2_score', 0)
                is_addiction = 'addict' in target_name.lower()
                icon = "🧠" if is_addiction else "🔮"
                
                insights += f"{icon} **OPTIMISATION DU MODÈLE ({target_pretty}):**\n"
                
                if r2 > 0.7:
                    insights += f"• **Modèle très fiable (R²={r2:.3f})** - Utilisation opérationnelle recommandée\n"
                    if is_addiction:
                        insights += f"• **Action:** Déployez une alerte automatique pour les scores >8/10 et contactez les étudiants concernés.\n"
                        insights += f"• **Prévention:** Suivez hebdomadairement les profils à risque et offrez des ateliers bien-être.\n"
                    else:
                        insights += f"• **Action:** Prédisez les performances de vos 10 prochains posts avant publication\n"
                        insights += f"• **Optimisation:** Ajustez les variables pour maximiser les prédictions\n"
                elif r2 > 0.5:
                    insights += f"• **Modèle modérément fiable (R²={r2:.3f})** - Amélioration possible\n"
                    insights += f"• **Action:** Collectez 50% de données supplémentaires et diversifiez les variables explicatives\n"
                    if is_addiction:
                        insights += f"• **Suivi:** Combinez ces scores avec des indicateurs qualitatifs (stress, sommeil) pour affiner les alertes.\n"
                else:
                    insights += f"• **Modèle peu fiable (R²={r2:.3f})** - Facteurs cachés\n"
                    insights += f"• **Action:** Analysez les variables manquantes (type d'activité, contexte scolaire)\n"
                    if not is_addiction:
                        insights += f"• **Recherche:** Testez l'engagement émotionnel vs quantitatif\n"
                
                insights += "\n"
        
        # 4. PLAN D'ACTION OPÉRATIONNEL
        insights += f"📋 **PLAN D'ACTION IMMÉDIAT (7 JOURS):**\n"
        insights += f"• **Jour 1-2:** Analysez vos 10 meilleurs posts et identifiez les patterns\n"
        insights += f"• **Jour 3-4:** Créez 5 nouveaux posts en appliquant les insights\n"
        insights += f"• **Jour 5-6:** Testez les recommandations sur 2 plateformes\n"
        insights += f"• **Jour 7:** Mesurez les résultats et ajustez la stratégie\n\n"
        
        insights += f"📊 **KPIs À SUIVRE (30 JOURS):**\n"
        insights += f"• Engagement moyen par plateforme\n"
        insights += f"• Taux de croissance des followers\n"
        insights += f"• Performance des nouveaux formats testés\n"
        insights += f"• ROI des optimisations appliquées\n\n"
        
        insights += f"🎯 **OBJECTIFS QUANTIFIÉS:**\n"
        if platform_comparison is not None and len(platform_comparison) > 0:
            current_avg = platform_comparison['mean_engagement'].mean()
            target = current_avg * 1.3  # +30% d'amélioration
            insights += f"• Augmenter l'engagement moyen de {current_avg:.2f}% à {target:.2f}% (+30%)\n"
            insights += f"• Améliorer la plateforme la plus faible de 50%\n"
            insights += f"• Atteindre 5% d'engagement sur la meilleure plateforme\n"
        
        return insights
    
    def generate_content_recommendation(self, platform, avg_engagement, is_premium=False):
        """Génère des recommandations de contenu pour une plateforme"""
        if not is_premium:
            return f"Taux d'engagement actuel sur {platform}: {avg_engagement:.2f}%. Passez en Premium pour des recommandations détaillées."
        
        recommendations = {
            'tiktok': "Pour TikTok: Privilégiez les vidéos courtes (15-30s), utilisez des trending sounds, postez entre 18h-21h.",
            'instagram': "Pour Instagram: Alternez Reels et Stories, utilisez 20-30 hashtags pertinents, postez à 11h et 19h.",
            'facebook': "Pour Facebook: Partagez du contenu vidéo natif, posez des questions pour générer des commentaires, postez en début d'après-midi.",
            'twitter': "Pour Twitter: Tweetez fréquemment (3-5x/jour), utilisez des images/GIFs, engagez dans les trending topics.",
            'youtube': "Pour YouTube: Créez des miniatures attractives, utilisez des titres accrocheurs, publiez régulièrement (même jour/heure).",
            'linkedin': "Pour LinkedIn: Partagez votre expertise, postez le mardi-jeudi matin, utilisez des documents PDF/carrousels."
        }
        
        platform_lower = platform.lower()
        base_rec = recommendations.get(platform_lower, "Analysez votre audience et testez différents types de contenu.")
        
        # Ajouter des conseils basés sur l'engagement
        if avg_engagement < 2:
            base_rec += " ⚠️ Engagement faible: Revoyez votre stratégie de contenu et votre timing."
        elif avg_engagement > 5:
            base_rec += " 🎉 Excellent engagement! Continuez ainsi et analysez ce qui fonctionne."
        
        return base_rec
    
    def explain_metric(self, metric_name, is_premium=False):
        """Explique une métrique spécifique"""
        explanations = {
            'engagement_rate': {
                'basic': "Taux d'engagement = (Interactions / Followers) × 100. Plus c'est élevé, mieux c'est!",
                'premium': "Le taux d'engagement mesure l'interaction de votre audience. Formule: (Likes + Commentaires + Partages) / Followers × 100. Un bon taux varie de 1-5% selon la plateforme. Au-dessus de 5% = excellent, en-dessous de 1% = à améliorer."
            },
            'likes': {
                'basic': "Nombre de likes reçus sur vos publications.",
                'premium': "Les likes indiquent l'appréciation du contenu. Ils sont corrélés avec la portée, mais ne garantissent pas l'engagement profond. Combinez avec commentaires et partages pour une vue complète."
            },
            'reach': {
                'basic': "Nombre de personnes qui ont vu votre contenu.",
                'premium': "La portée (reach) mesure l'audience unique touchée. Organique = gratuit via algorithme. Payant = via publicité. Un bon ratio Engagement/Reach (>3%) indique un contenu de qualité."
            },
            'impressions': {
                'basic': "Nombre total de fois où votre contenu a été affiché.",
                'premium': "Impressions vs Reach: Les impressions comptent chaque affichage (même multiple par personne), le reach compte les personnes uniques. Ratio Impressions/Reach élevé = contenu vu plusieurs fois = bon signe!"
            }
        }
        
        metric_lower = metric_name.lower()
        if metric_lower in explanations:
            return explanations[metric_lower]['premium' if is_premium else 'basic']
        else:
            return f"Métrique: {metric_name}. Passez en Premium pour des explications détaillées."
    
    def interpret_addiction_score(self, score):
        """Retourne un texte et un statut simple pour un score d'addiction."""
        if score is None:
            return "Score d'addiction indisponible. Veuillez relancer la prédiction.", "modéré"
        
        if score >= 8:
            text = ("Score critique : le risque d'addiction est très élevé. "
                    "Planifiez une intervention immédiate, proposez un accompagnement psychologique et réduisez l'exposition aux plateformes.")
            status = "critique"
        elif score >= 6:
            text = ("Score élevé : les signes d'addiction se renforcent. "
                    "Mettez en place des limites quotidiennes, surveillez le sommeil et encouragez des activités hors ligne.")
            status = "élevé"
        else:
            text = ("Score modéré : situation sous contrôle. "
                    "Continuez la sensibilisation et gardez un suivi régulier pour éviter toute dérive.")
            status = "modéré"
        
        return text, status

