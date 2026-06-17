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

### Verse 1 (Bramha 0.3741)
- **Original**: हमारा सनातन के 0 हम केक 4" ऑल अणे का. दो पास जाकर उत्तम अमृतकी 8 + पिदासे होन
- **Translation**: 

---

### Verse 2 (Bramha 0.3742)
- **Original**: याचना की। सोमने उन्हें बहुत उत्तम अमृत दिया पा > उलफनमीव+ की एव और
- **Translation**: 

---

### Verse 3 (Bramha 0.3743)
- **Original**: और वनस्पतियोंने वह लाकर बालकको दे दिया। आलकको अपने औरस पुत्रोके समान देखते #बैरअर उसी भावसे रक्षा करते हैं, वे निश्चय ही ब्रह्मा आदि
- **Translation**: 

---

### Verse 4 (Bramha 0.3744)
- **Original**: 48. झ्म # 258 -37*3:4 (पल #ब यों कस बालकको
- **Translation**: 

---

### Verse 5 (Bramha 0.3745)
- **Original**: किया था, इसलिये वह पिप्पलादके नामसे प्रसिद्ध पीपलके समीप रख दिया और स्वामीमें चित्त
- **Translation**: 

---

### Verse 6 (Bramha 0.3746)
- **Original**: हुआ। बढ़ा होनेपर काव्य सनम. 4 लगाकर अग्निको प्रणाम किया; फिर अग्निकी
- **Translation**: 

---

### Verse 7 (Bramha 0.3747)
- **Original**: अत्यन्त विस्मित होकर कहा-- कक परिक्रमा करके यज्ञपाश्रेंक साथ ही चितामें प्रवेश
- **Translation**: 

---

### Verse 8 (Bramha 0.3748)
- **Original**: जाता है कि मनुष्योंसे मनुष्य, पक्षियोंसे : .._+ उत्पदाते यतु विनाशि सर्वे न शोच्यमस्तीति मनुष्यलोके । जा आओ
- **Translation**: 

---

### Verse 9 (Bramha 0.3749)
- **Original**: राणा: सर्केहस्पापि देहान्वितस्प यातारों वै नात्र संदेहलेश: । एबं ज्ञात्वा विप्रगोदेवदीताद्यर्थ बा न 5वकवमर $ये बालक मातृपितृप्रहोण॑ सनिर्बिशेष॑ स्वतनुप्ररूढ़ै:। पश्यन्ति रक्षन्ति त एय नूत॑ कऋद्मादिकातामपि 1: ; # स्वर्गमासेदुषो: पिज्रोस्तदपत्देष्यकृत्रिमम्‌। ये कुर्वन्त्थनिशं स्‍्तेहें ठ एक. कृतिनों नराः
- **Translation**: 

---

### Verse 10 (Bramha 0.3750)
- **Original**: रै8ंड * संक्षिप्त श्रह्मपुराण « वनस्पतियोंसे वनस्पति उत्पन्न होते हैं; इसमें कहीं
- **Translation**: 

---

### Verse 11 (Bramha 0.3751)
- **Original**: भीषण कृत्या पिप्पलादसे बोली-- 'बताओ, मुझे विषमता नहीं दिखायी देती। परंतु मैं वृक्षका पुत्र
- **Translation**: 

---

### Verse 12 (Bramha 0.3752)
- **Original**: क्या करना है?' पिप्पलादने कहा-- “देवता मेरे होकर हाथ-पैर आदिसे विशिष्ट जीव कैसे हो
- **Translation**: 

---

### Verse 13 (Bramha 0.3753)
- **Original**: शत्रु हैं। उन्हें खा जा।' फिर तो उस बडवाके गया!' उनकी बात सुनकर वृक्षोंने क्रमशः उनके
- **Translation**: 

---

### Verse 14 (Bramha 0.3754)
- **Original**: गर्भसे महाभयंकर अग्नि प्रकट हुई, जो समस्त पिता दधीचिकी मृत्यु और पतिब्रता माताके
- **Translation**: 

---

### Verse 15 (Bramha 0.3755)
- **Original**: लोकोंका प्रलय करनेमें समर्थ थी। देवता उसे अग्निप्रवेशका सब समाचार कह सुनाया। सुनते
- **Translation**: 

---

### Verse 16 (Bramha 0.3756)
- **Original**: देखते ही थर्रा उठे और पिप्पलादद्वारा आराधित ही वे दुःखसे व्याप्त होकर पृथ्वीपर गिर पढ़े। उस
- **Translation**: 

---

### Verse 17 (Bramha 0.3757)
- **Original**: पिप्पलेश नामसे प्रसिद्ध भगवान्‌ शिवक्ौं शरणमें समय वृक्षोंने धर्म और अर्थयुक्त वचन कहकर
- **Translation**: 

---

### Verse 18 (Bramha 0.3758)
- **Original**: आये। उन्होंने भयभीत होकर शिवजीकी स्तुति उन्हें सान्त्वना दी। आश्वस्त होनेपर उन्होंने ओषधियों
- **Translation**: 

---

### Verse 19 (Bramha 0.3759)
- **Original**: करते हुए कहा--'शम्भो ! आप हमारी रक्षा करें। और वनस्पतियोंसे कहा, ' जिन्होंने मेरे पिताकी
- **Translation**: 

---

### Verse 20 (Bramha 0.3760)
- **Original**: कृत्या और उससे प्रकट हुई आग हमें बड़ा कष्ट हत्या की है, उनका मैं भी वध करूँगा, अन्यथा
- **Translation**: 

---

