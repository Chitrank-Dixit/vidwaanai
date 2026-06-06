# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Markende Puran 0.2861)
- **Original**: 622! अवलिप्तासि मैन त्वं देवि ब्लूहि ममाग्रत:। तैलोक्ये क: पुमांस्मिप्ेदग्े शुम्भनिशुम्भयो:
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2862)
- **Original**: अन्येषापपि हैल्यानां सर्वे देखा न वै युधि। तिएनन्ति सम्मुखे देवि किं पुनः स्त्री त्यमेकिका
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2863)
- **Original**: इन्द्राद्या: सकला देशास्तस्थुर्वेषां न संयुगे। शुम्भादीनां कर तेषां स्त्री फ्रयास्यसि सम्मुखपू
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2864)
- **Original**: * संक्षिप्त भार्कण्डेयपुराण * 7क56# & # 477 # 7477 0 00:81 22 रा 242 44 6:54 फेक & कक # 27 20070 क 02 203 722 शा 7 अत सा त्व॑ गच्छ परयैवोक्ता पार्श्व शुम्भनिशुम्भयो:
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2865)
- **Original**: केशाकर्षणनिर्धूतगौरवा मा गमिष्यसि
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2866)
- **Original**: दूत बोला--
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2867)
- **Original**: देवि! तुम घमंडमें भरी हो, मेरे सामने ऐसी बातें न करो। तीनों लोकोंमें कौन ऐसा पुरुष है, जो शुम्भ- निशुम्भके स्रामने खड़ा हो सके
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2868)
- **Original**: देवि। अन्य दैत्योंके सामने भी स्रारे देजता युद्धमें नहीं ठहर सकते, फिर तुम अकेली स्त्री होकर कैसे ठहर सकती हो
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2869)
- **Original**: जिन शुम्भ आदि दत्योंके सामने इन्द्र आदि देवता भी युद्धमें ख़ड़े नहों हुए, उनके सामने तुम स्त्री होकर कैसे जाओगी
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2870)
- **Original**: इसलिये तुम पेरे ही कहनेसे शुम्भ-निशुम्भके पास चली चलो। ऐसा करनेसे तुम्हारे गौरबकी रक्षा होगी; अन्यथा जब वे केश पकड़कर घसीटेंगे, तब तुम्हें अपनी प्रतिष्ठा खाकर जाना पड़ेगा
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2871)
- **Original**: देव्युबाच
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2872)
- **Original**: एव्म्रेतद्‌ बली शुष्भो निशुम्भश्चातिवीर्यवान्‌। किं करोपि प्रतिज्ञा मे यदवालोचिता पुरा
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2873)
- **Original**: स त्व॑ं गच्छ मयोक्त ते यदेतत्सर्वमादृतः। तदाचश्ष्वासुरेद्ाय स॒ च युक्त करोतु वते
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2874)
- **Original**: देवीने कहा--
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2875)
- **Original**: तुम्हारा कहना ठीक है, शुम्भ ऋलवान्‌ हैं और निशुम्म भी बड़े पराक्रमी हैं; किंतु क्या करूँ। पैने पहले बिना सोचे-समझे प्रतिज्ञा कर ली है
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2876)
- **Original**: अतः अब तुम जाओ; मैंदे तुपसे जो कुछ कहा है, बह सब दँत्वराजसे आदरपूर्वबक कहना। फिर वे जो उचित जान पड़े, करें
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2877)
- **Original**: जत्ि अपार्कण्डेयपुराणे साकर्णिके यन्वन्तरे देवीसाह्मत्वे देव्या वृत्संबादों गम पस्मोथ्याय:
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2878)
- **Original**: 54 उकाक्र 9, क़िग्रमज्ा: 56. सलोकाः 54 एक्मू 129, यवगावितः #इटट
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2879)
- **Original**: # इस प्रकार श्रीमार्केण्डेयपुराणपें साथर्णिक मन्वन्तरक्री कथाके अन्तर्गत देवीमाहात्म्यमें 'देखी-दूत-संवाद ' नामक पाँचवाँ अध्याय पूरा हुआ
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2880)
- **Original**: + 50%. 5, पा0-यत्‌।
- **Translation**: 

---

