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

### Verse 1 (Markende Puran 0.2841)
- **Original**: <- शक यह या थे, ते सत्र मेरे हो पास आ गये हैं
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2842)
- **Original**: देत्रि! हमलोग तुए्हें स॑सारकी स्त्रियोंमें (तन मानते हैं, अतः तुम हमारे पास आ जाओ; क्योंकि रत्नोंका उपभोग ऋरणेबलें हम ही हैं
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2843)
- **Original**: चम्ल करटक्षोंबाली सझुन्दरीं! तुम मेरों था मेरे भाई महाप्रराक्रमों विशुम्भकों सेवामें आ जाओ; क्योंकि तुम रत्नस्थरूपा हो
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2844)
- **Original**: मेरा करण करनेसे त्रुम्हें तुलनारहित महान्‌ ऐश्वर्यकौ प्राप्ति होगी। अपनी बरुड्धिसे बह बिचार कर तुम पेरों पत्नो लन जाओ'
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2845)
- **Original**: क्रयिकताणच
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2846)
- **Original**: 115 / इल्युक्ता सा ददा देवी ग्भीरान्तःस्मिता जगौ। दुर्णा भगवती धदट्ठा चयेर्द धार्यते जगत्‌
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2847)
- **Original**: ऋषि कहते हैं--
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2848)
- **Original**: दूतके योाँ कहरेपर कल्थाणमयी भगवतों दुगदिवी, जो इस जहूगत्‌ृकों धारण करतो हैं, भन- हों सन गम्भीर भाक मुस्करायीं और इस प्रकार
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2849)
- **Original**: 290 ह00, 4.3.
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2850)
- **Original**: & 3, / ह//7/ 4 4 / 3 ब्ेव्युजाच
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2851)
- **Original**: सत्यमुक्त त्वया नात्र मिथ्या किंचित्तयोदितप्‌। तैलोकयाथिपत्ति: शुप्धो निशुष्पश्चापि तादूशः
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2852)
- **Original**: कि त्वत्र यग्प्रतिज्ञा्ं मिध्यां तत्करिचते कथप्‌। श्रुयतामल्पबुद्धित्वात्प्रतिज्ञा या कृता पुरा
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2853)
- **Original**: यो मां जबति संग्राम्रे यो मे दर्प व्यपोहति। यो मे प्रतिबलो लोके स मे भर्ता भविष्यति
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2854)
- **Original**: न्दागच्छततु शुब्भोउत्र निशुष्भो वा महासुर:। मां जिल्वा किं चिरेणात्र पाणिं गह्नातु मे लघु
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2855)
- **Original**: देवीने कहा--
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2856)
- **Original**: दूत! तुपने सत्य कहा है, इसमें तनिक भी मिथ्था नहीं है। शुघ्भ तीनों ज्ञोकौंका स्वामी है और निशुम्भ भो उम्रीके सपान पराक्रमी है
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2857)
- **Original**: किंतु इस विमयमें मैंने जो प्रत्तिज़ां कर ली है, उसे मिथ्या कैंसें करूं। मैंने अपनी अल्पचुद्धिके कारण पहलेसे जो प्रतिज्ञा कर रखी है, उसको स्रुनों
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2858)
- **Original**: 'जो मुझे संग्राममें जीत लेगा, जो मेरे अभिमानकों चूर्ण कर देगा तथा संसारमें जो मेरे समान बलवान होगा, कहीं पेण स्वामी होगा'
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2859)
- **Original**: इसलिये शुम्भ अथब! पहादँत्य निशुम्भ स्वयं ही यहाँ पध्चारें और मुझे जीतकर शीघ्र ही मेरा पाणिग्रहण कर लें, इसमें त्रिल्लम्बकों क्या आवश्यकता है
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2860)
- **Original**: दूठ डवाच
- **Translation**: 

---

