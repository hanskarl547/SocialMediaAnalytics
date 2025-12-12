"""
Assistant IA Amélioré avec Interprétations Basées sur des Cas Réels
Version avancée avec insights concrets et recommandations actionables
"""

import openai
import os
from dotenv import load_dotenv
from real_world_ai_interpreter import RealWorldAIInterpreter

load_dotenv()

class EnhancedAIAssistant:
    def __init__(self):
        """Initialise l'assistant IA amélioré"""
        self.api_key = os.getenv('OPENAI_API_KEY', '')
        if self.api_key:
            openai.api_key = self.api_key
        self.real_world_interpreter = RealWorldAIInterpreter()
    
    def interpret_results(self, analysis_results, is_premium=False, platform_comparison=None):
        """
        Interprète les résultats d'analyse avec IA basée sur des cas réels
        
        Parameters:
        analysis_results (dict): Résultats des tests statistiques
        is_premium (bool): Si l'utilisateur est premium
        platform_comparison (DataFrame): Comparaison des plateformes
        """
        # Utiliser l'IA basée sur des cas réels en priorité
        real_world_interpretation = self._get_real_world_interpretation(analysis_results, is_premium, platform_comparison)
        
        # Si OpenAI est disponible et premium, enrichir avec GPT
        if self.api_key and is_premium:
            try:
                enhanced_interpretation = self._enhance_with_openai(real_world_interpretation, analysis_results)
                return enhanced_interpretation
            except Exception as e:
                print(f"Erreur OpenAI: {e}")
                return real_world_interpretation
        
        return real_world_interpretation
    
    def _get_real_world_interpretation(self, analysis_results, is_premium=False, platform_comparison=None):
        """Obtient l'interprétation basée sur des cas réels"""
        
        interpretation = "📊 **ANALYSE APPROFONDIE DES RÉSULTATS**\n\n"
        
        # Analyser chaque type de test
        for test_name, result in analysis_results.items():
            if test_name == 'kruskal_wallis' and result:
                interpretation += self.real_world_interpreter.interpret_kruskal_wallis_real_world(result, platform_comparison)
                interpretation += "\n" + "="*60 + "\n\n"
            
            elif test_name == 'spearman' and result:
                interpretation += self.real_world_interpreter.interpret_spearman_real_world(result, 'likes', 'engagement_rate')
                interpretation += "\n" + "="*60 + "\n\n"
            
            elif test_name == 'friedman' and result:
                interpretation += self.real_world_interpreter.interpret_friedman_real_world(result)
                interpretation += "\n" + "="*60 + "\n\n"
        
        # Ajouter des insights généraux
        interpretation += self._add_general_insights(analysis_results, platform_comparison)
        
        return interpretation
    
    def _enhance_with_openai(self, base_interpretation, analysis_results):
        """Enrichit l'interprétation avec OpenAI"""
        
        prompt = f"""
        Vous êtes un expert en marketing digital et analyse de données des réseaux sociaux avec 10+ ans d'expérience.
        
        Voici une analyse basée sur des cas réels et des benchmarks de l'industrie :
        
        {base_interpretation}
        
        Veuillez enrichir cette analyse avec :
        1. Des exemples concrets d'entreprises qui ont réussi avec des stratégies similaires
        2. Des prédictions de ROI basées sur les données et l'expérience
        3. Des conseils tactiques spécifiques pour l'implémentation
        4. Des métriques de suivi recommandées avec des seuils précis
        5. Des alertes sur les risques potentiels et comment les éviter
        6. Des comparaisons avec les standards de l'industrie
        
        Gardez un ton professionnel mais accessible, avec des recommandations actionables et des chiffres concrets.
        """
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Vous êtes un expert en marketing digital avec 10+ ans d'expérience dans l'analyse des réseaux sociaux. Vous avez travaillé avec des marques comme Nike, Coca-Cola, et des startups tech."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1200,
                temperature=0.7
            )
            
            enhanced_content = response.choices[0].message.content
            
            # Combiner les deux interprétations
            final_interpretation = base_interpretation + "\n\n" + "🤖 **ENRICHISSEMENT IA AVANCÉ**\n\n" + enhanced_content
            
            return final_interpretation
            
        except Exception as e:
            print(f"Erreur lors de l'enrichissement OpenAI: {e}")
            return base_interpretation
    
    def _add_general_insights(self, analysis_results, platform_comparison):
        """Ajoute des insights généraux basés sur les résultats"""
        
        insights = "🎯 **INSIGHTS GÉNÉRAUX ET RECOMMANDATIONS**\n\n"
        
        # Analyser la qualité globale des données
        total_tests = len(analysis_results)
        significant_tests = sum(1 for result in analysis_results.values() if result and result.get('significant', False))
        
        insights += f"📊 **QUALITÉ DE L'ANALYSE:**\n"
        insights += f"• {total_tests} tests effectués\n"
        insights += f"• {significant_tests} résultats significatifs\n"
        insights += f"• Taux de significativité: {significant_tests/total_tests*100:.1f}%\n\n"
        
        # Recommandations basées sur la significativité
        if significant_tests >= total_tests * 0.7:
            insights += "🌟 **EXCELLENTE QUALITÉ DES DONNÉES**\n"
            insights += "• Vos données sont très fiables pour la prise de décision\n"
            insights += "• Vous pouvez implémenter les recommandations avec confiance\n"
            insights += "• Surveillez les métriques clés toutes les semaines\n\n"
        elif significant_tests >= total_tests * 0.5:
            insights += "✅ **BONNE QUALITÉ DES DONNÉES**\n"
            insights += "• Vos données sont généralement fiables\n"
            insights += "• Implémentez les recommandations principales\n"
            insights += "• Collectez plus de données pour les analyses non-significatives\n\n"
        else:
            insights += "⚠️ **QUALITÉ DES DONNÉES À AMÉLIORER**\n"
            insights += "• Collectez plus de données avant de prendre des décisions majeures\n"
            insights += "• Concentrez-vous sur les analyses significatives\n"
            insights += "• Revoyez votre stratégie de collecte de données\n\n"
        
        # Insights sur les plateformes
        if platform_comparison is not None and not platform_comparison.empty:
            insights += "📱 **ANALYSE DES PLATEFORMES:**\n"
            
            # Trouver la meilleure et la pire plateforme
            best_platform = platform_comparison.loc[platform_comparison['mean_engagement'].idxmax()]
            worst_platform = platform_comparison.loc[platform_comparison['mean_engagement'].idxmin()]
            
            insights += f"• Meilleure plateforme: {best_platform['platform']} ({best_platform['mean_engagement']:.2f}%)\n"
            insights += f"• Plateforme à améliorer: {worst_platform['platform']} ({worst_platform['mean_engagement']:.2f}%)\n"
            insights += f"• Écart de performance: {best_platform['mean_engagement'] - worst_platform['mean_engagement']:.2f}%\n\n"
            
            # Recommandations spécifiques
            insights += "💡 **RECOMMANDATIONS STRATÉGIQUES:**\n"
            insights += f"• Investissez 60% de vos ressources sur {best_platform['platform']}\n"
            insights += f"• Revoyez complètement votre stratégie sur {worst_platform['platform']}\n"
            insights += f"• Analysez les différences entre les plateformes pour optimiser\n\n"
        
        # Plan d'action
        insights += "🚀 **PLAN D'ACTION RECOMMANDÉ:**\n"
        insights += "**Semaine 1-2:** Analyse approfondie des données\n"
        insights += "**Semaine 3-4:** Implémentation des optimisations\n"
        insights += "**Semaine 5-6:** Mesure et ajustement\n"
        insights += "**Semaine 7-8:** Standardisation des meilleures pratiques\n\n"
        
        # Métriques de suivi
        insights += "📈 **MÉTRIQUES DE SUIVI RECOMMANDÉES:**\n"
        insights += "• Taux d'engagement par plateforme (hebdomadaire)\n"
        insights += "• Croissance des followers (mensuelle)\n"
        insights += "• Performance des contenus (quotidienne)\n"
        insights += "• ROI des campagnes (mensuelle)\n\n"
        
        return insights
    
    def generate_content_recommendation(self, platform, engagement_rate, is_premium=False):
        """Génère des recommandations de contenu basées sur des cas réels"""
        
        # Obtenir les benchmarks réels
        benchmarks = self.real_world_interpreter.get_industry_benchmarks(platform, 'engagement_rates')
        
        if not benchmarks:
            return f"Pour {platform}: Optimisez votre stratégie de contenu pour améliorer l'engagement."
        
        # Déterminer le niveau de performance
        if engagement_rate >= benchmarks.get('excellent', 0):
            performance_level = "excellent"
            emoji = "🌟"
        elif engagement_rate >= benchmarks.get('good', 0):
            performance_level = "bon"
            emoji = "✅"
        elif engagement_rate >= benchmarks.get('average', 0):
            performance_level = "moyen"
            emoji = "⚠️"
        else:
            performance_level = "faible"
            emoji = "❌"
        
        # Obtenir les stratégies de contenu
        content_strategies = self.real_world_interpreter.get_content_strategies(platform)
        
        recommendation = f"Pour {platform}: {emoji} Performance {performance_level} ({engagement_rate:.1f}%)\n"
        
        if performance_level == "excellent":
            recommendation += f"🎉 Excellent engagement! Continuez ainsi et analysez ce qui fonctionne.\n"
            recommendation += f"💡 Stratégies recommandées: {', '.join(content_strategies[:2])}\n"
        elif performance_level == "bon":
            recommendation += f"📈 Bon engagement! Optimisez pour atteindre l'excellence.\n"
            recommendation += f"💡 Stratégies recommandées: {', '.join(content_strategies[:3])}\n"
        elif performance_level == "moyen":
            recommendation += f"📊 Engagement moyen. Revoyez votre stratégie de contenu.\n"
            recommendation += f"💡 Stratégies recommandées: {', '.join(content_strategies)}\n"
        else:
            recommendation += f"⚠️ Engagement faible. Révision complète nécessaire.\n"
            recommendation += f"💡 Stratégies recommandées: {', '.join(content_strategies)}\n"
        
        # Ajouter des conseils spécifiques
        if platform == 'TikTok':
            recommendation += f"🎵 Conseils TikTok: Utilisez des trending sounds, postez 2-3x/jour, créez des défis\n"
        elif platform == 'Instagram':
            recommendation += f"📸 Conseils Instagram: Alternez Reels et Stories, utilisez 20-30 hashtags pertinents\n"
        elif platform == 'Facebook':
            recommendation += f"📘 Conseils Facebook: Partagez du contenu vidéo natif, posez des questions\n"
        
        return recommendation
    
    def explain_metric(self, metric_name, is_premium=False):
        """Explique une métrique avec des exemples concrets"""
        
        explanations = {
            'engagement_rate': {
                'definition': 'Le taux d\'engagement mesure l\'interaction de votre audience',
                'formula': '(Likes + Commentaires + Partages) / Followers × 100',
                'benchmarks': 'TikTok: 3-9%, Instagram: 1.5-4.7%, Facebook: 1-3%',
                'example': 'Si vous avez 1000 followers et 50 interactions, votre taux = 5%',
                'action': 'Un bon taux varie de 1-5% selon la plateforme'
            },
            'likes': {
                'definition': 'Les likes indiquent l\'appréciation du contenu',
                'formula': 'Nombre total de likes sur un post',
                'benchmarks': 'Dépend de votre audience et du type de contenu',
                'example': 'Un post viral peut avoir 10,000+ likes',
                'action': 'Combinez avec commentaires et partages pour une vue complète'
            },
            'reach': {
                'definition': 'La portée mesure l\'audience unique touchée',
                'formula': 'Nombre de personnes uniques qui ont vu votre contenu',
                'benchmarks': 'Organique vs Payant: ratio idéal 70/30',
                'example': 'Si 500 personnes voient votre post, votre reach = 500',
                'action': 'Un bon ratio Engagement/Reach (>3%) indique un contenu de qualité'
            },
            'impressions': {
                'definition': 'Les impressions comptent chaque affichage du contenu',
                'formula': 'Nombre total d\'affichages (peut inclure plusieurs vues par personne)',
                'benchmarks': 'Ratio Impressions/Reach élevé = bon signe',
                'example': 'Si votre post est vu 3 fois par 100 personnes, impressions = 300',
                'action': 'Ratio Impressions/Reach élevé = contenu vu plusieurs fois = bon signe!'
            }
        }
        
        if metric_name.lower() in explanations:
            metric = explanations[metric_name.lower()]
            explanation = f"**{metric_name.upper()}:**\n"
            explanation += f"{metric['definition']}. {metric['formula']}. {metric['benchmarks']}. {metric['example']}. {metric['action']}."
            return explanation
        else:
            return f"**{metric_name.upper()}:** Métrique importante à surveiller pour optimiser vos performances."
    
    def get_industry_benchmarks(self, platform, metric):
        """Retourne les benchmarks de l'industrie"""
        return self.real_world_interpreter.get_industry_benchmarks(platform, metric)
    
    def get_content_strategies(self, platform):
        """Retourne les stratégies de contenu recommandées"""
        return self.real_world_interpreter.get_content_strategies(platform)
    
    def get_algorithm_factors(self, platform):
        """Retourne les facteurs algorithmiques"""
        return self.real_world_interpreter.get_algorithm_factors(platform)


