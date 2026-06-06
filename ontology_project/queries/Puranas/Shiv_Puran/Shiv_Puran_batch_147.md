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

### Verse 1 (Shiv Puran 0.2921)
- **Original**: ज्येष्ना बरिष्ठा वरदा दिवयोर्यजने स्ता। तयोराज्ञौं पुरस्कृत्य सा में दिफ्तु काज्लितम
- **Translation**: 

---

### Verse 2 (Shiv Puran 0.2922)
- **Original**: सर्वश्रेष्ठ और वरदाचिनी ज्येष्ठादेजी, जो सदा भगवान्‌ शिव और पार्य॑तीके पूजनपें रूगी रहती हैं, उन दोनॉकी आज्ञा मानकर मुझे मनोवाज्छित वस्तु प्रदान करें
- **Translation**: 

---

### Verse 3 (Shiv Puran 0.2923)
- **Original**: तऔैल्ग्रेक्यअन्दिता साक्षादुल्काकारा गणाम्बिका
- **Translation**: 

---

### Verse 4 (Shiv Puran 0.2924)
- **Original**: जगत्सृष्टिविव॒ुद््‌यर्थ ऋद्मणाभ्यर्थिता दिवात्‌
- **Translation**: 

---

### Verse 5 (Shiv Puran 0.2925)
- **Original**: झिलाया:. प्रतिषक्ताया.. ध्रुवोरनत्तरनिस्पृता
- **Translation**: 

---

### Verse 6 (Shiv Puran 0.2926)
- **Original**: दाक्षायणी सती मेना तथा हैमजती ह्युमा
- **Translation**: 

---

### Verse 7 (Shiv Puran 0.2927)
- **Original**: कौरिक्याईैत जतनी भद्धकाल्यास्तवैत्र च। अपर्णयाश्ष कननी पाटस्त्रयात्तथैव च
- **Translation**: 

---

### Verse 8 (Shiv Puran 0.2928)
- **Original**: जिवार्चनस्ता नित्य रुद्राणी रुद्रबल्‍्लकभा
- **Translation**: 

---

### Verse 9 (Shiv Puran 0.2929)
- **Original**: सत्कत्य शिवयोशज्ञों सा मे दिशतु काह्लितम
- **Translation**: 

---

### Verse 10 (Shiv Puran 0.2930)
- **Original**: छ्ट0 # संक्षिप्त क्र <.52322*%0##/#*##ै##ऋक कै 0%00%$%%$*+++4#4/#24440/04 747 टै सै ## कै कै कै के के कै कै कक के # कै #/##'॑॑ऋ4॑ज॑ 4 # जैल्मेक्यबन्दिता, . साक्षात्‌. उल्का (लुकाठी ) जैसी आकृत्तिवाली गणाम्बिकां, जो जगतकी सृष्टि बढ़ानेके आज्ञा शिरोधार्य करके मुझे मनोब्राब्छित चंण्ड:.. सर्वगणेशाग: हाम्मोर्कदनसण्पय: । पिजले गणफः श्रीमाज्‌ शिवासक्त: दिवप्रियः
- **Translation**: 

---

### Verse 11 (Shiv Puran 0.2931)
- **Original**: आज्षया शिवयोरेतव स में कार प्रयच्छत्‌
- **Translation**: 

---

### Verse 12 (Shiv Puran 0.2932)
- **Original**: भगवान्‌ शिवमें आसक्त और दिवके प्रिय गणपाल श्रीमान्‌ पिज्ुल झिव और शिवाक्री आज्ञासे ही मेरी मनःकामना पूर्ण करें
- **Translation**: 

---

### Verse 13 (Shiv Puran 0.2933)
- **Original**: भृद्जीओों नाम गणप: शिवाशधनतत्परः। प्रवच्छतु स्॒ में क्रम पत्युराज्ञाप्रस्सर्म्‌
- **Translation**: 

---

### Verse 14 (Shiv Puran 0.2934)
- **Original**: शिवकी आराधनापें तत्पर रहनेयाले भुदट्ढीश्वर नामक गणपाल् अपने स्वामीकी आज्ञा ले मुझे मनोवाड्छित यसस्‍्तु प्रदान करें
- **Translation**: 

---

### Verse 15 (Shiv Puran 0.2935)
- **Original**: । चीरभदों महातवेज्य हिंगकुल्देन्दुसनिफः । भदकाल्तप्रियों नित्य॑ महतृ्णों चानिरक्षिता
- **Translation**: 

---

### Verse 16 (Shiv Puran 0.2936)
- **Original**: यज्ञग्य च दिरोहतों दक्षास्य च दुरात्मन:। उफेब्द्रेन्ड्रयमादीनो देवानायक्ुतक्षकः
- **Translation**: 

---

### Verse 17 (Shiv Puran 0.2937)
- **Original**: सित्रयो: शासनाटरेब स में दिवातु काह्वितम्‌
- **Translation**: 

---

### Verse 18 (Shiv Puran 0.2938)
- **Original**: उ्म्ज्क्ल्ल, प्रातृशणोंकी रक्षा करनेवाले; दुरात्मा दक्ष और उसके बज्ञका सिर काटनेवाले; उपेन्द्र, इज और यम आदि देवताओंके अज्जॉमें घाव कर देनेवाले, झिवके अनुचर तथा शिवकी आज्ञाके पालक, महातेजस्वी श्रीमान्‌ वीरभद्र झिव और शिवाके आदेशसे ही मुझे मेरी मनचाही यस्‍्तु दें
- **Translation**: 

---

### Verse 19 (Shiv Puran 0.2939)
- **Original**: 83--85
- **Translation**: 

---

### Verse 20 (Shiv Puran 0.2940)
- **Original**: सरस्वती. गहेशस्थ वाक्सरोजसमुदझूवा
- **Translation**: 

---

