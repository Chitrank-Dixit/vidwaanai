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

### Verse 1 (Bramha 0.3961)
- **Original**: सोमको पतिरूपमें पाकर ओषधियाँ बहुत प्रसन्न अनुमान कौन कर सकता है, जिनके महापातकोंका
- **Translation**: 

---

### Verse 2 (Bramha 0.3962)
- **Original**: हुई थीं। उन्होंने सब लोगों तथा गज्जाजीके सामने नाश करनेवाली आप जगन्माता गड्ढा उनके लिये
- **Translation**: 

---

### Verse 3 (Bramha 0.3963)
- **Original**: यह अभीष्ट बचन कहा--'बेदमें एक पवित्र गाथा सदा ही सुलभ हैं। तीनों लोकोंकी बन्दनीया
- **Translation**: 

---

### Verse 4 (Bramha 0.3964)
- **Original**: है, जिसे वेदोंके विद्धान्‌ जानते हैं। जिस भूमिमें जगजननी गद्जा ! आपके वैभवको कोई नहीं
- **Translation**: 

---

### Verse 5 (Bramha 0.3965)
- **Original**: फसल ठगी हुई है, वह माताके समान किंवा जानता; क्योंकि कामदेवके शत्रु भगवान्‌ शंकर भी ; साक्षात्‌ माता ही है। जो गड्जाजीके समीप उसका आपको सदा मस्तकपर लिये रहते हैं। मनोवाज्छित
- **Translation**: 

---

### Verse 6 (Bramha 0.3966)
- **Original**: दान करता है, वह समस्त अभिलपित वस्तुओंको फल देनेबाली माता ! तुम्हें नमस्कार है। पापोंका
- **Translation**: 

---

### Verse 7 (Bramha 0.3967)
- **Original**: प्राप्त कर लेता है। जो मानव खेती लगी हुई भूमि, बिनाश करनेवाली ब्रह्ममयी देवी ! तुम्हें नमस्कार
- **Translation**: 

---

### Verse 8 (Bramha 0.3968)
- **Original**: गौ तथा ओषधियोंको ब्रह्मा, विष्णु एवं शिवरूप है। भगवान्‌ विष्णुके चरणकमलोंसे निकली हुई
- **Translation**: 

---

### Verse 9 (Bramha 0.3969)
- **Original**: ब्राष्मणके लिये भक्तिपूर्वक दान देता है, उसका गड्ढा ! तुम्हें नमस्कार है। भगवान्‌ शंकरकी
- **Translation**: 

---

### Verse 10 (Bramha 0.3970)
- **Original**: किया हुआ सब दान अक्षय होता है तथा वह जटासे प्रकट हुई गौतमी देवी! तुम्हें नमस्कार है।
- **Translation**: 

---

### Verse 11 (Bramha 0.3971)
- **Original**: अपने सम्पूर्ण अभीष्टोंको प्राप्त कर लेता है। इस प्रकार स्तुति करनेवाली ओषधियोंसे
- **Translation**: 

---

### Verse 12 (Bramha 0.3972)
- **Original**: ओषधियाँ सोम राजाकी प्रिया हैं और सोम भी गड्जाजीने कहा--' देवियो! बताओ, तुम्हें क्या दूँ ?”
- **Translation**: 

---

### Verse 13 (Bramha 0.3973)
- **Original**: ओषधियोंके पति हैं--यह जानकर जो ब्रह्मवेत्ता ओषधियाँ बोली-'जगन्माता ! हमें अत्यन्त
- **Translation**: 

---

### Verse 14 (Bramha 0.3974)
- **Original**: ब्राह्णणणो ओषधि (अन्न) दान करता है, वह तेजस्वी राजाकों पतिरूपमें दीजिये।” गद्भाजीने
- **Translation**: 

---

### Verse 15 (Bramha 0.3975)
- **Original**: सम्पूर्ण अभिलषित वस्तुओंको पाता और ब्राह्नलोकमें कहा--“माता ओषधियो ! मैं अमृतरूप हूँ। तुम ' प्रतिष्ठित होता है। ओषधियाँ राजा सोमसे बातचीत भी अमृतस्वरूपा हो। अतः तुम्हें तुम्हारे योग्य ही
- **Translation**: 

---

### Verse 16 (Bramha 0.3976)
- **Original**: करती हुई कहती हैं--'राजन्‌ ! हम ब्रह्मरूपिणी अमृतात्मा सोमको पतिरूपमें देती हूँ।' गौतमीके ' और प्राणरूपिणी हैं। जो हमें ब्राह्मणोंको दान इस बरदानका देवताओं, ऋषियों, चन्द्रमा तथा
- **Translation**: 

---

### Verse 17 (Bramha 0.3977)
- **Original**: करें, उसे तुम पार लगाओ। स्थावर-जज्जमरूप ओषधियोंने भी अनुमोदन किया। इसके बाद वे
- **Translation**: 

---

### Verse 18 (Bramha 0.3978)
- **Original**: जितना भी जगत्‌ है, वह सब हमलोगोंसे व्याप्त सब अपने-अपने स्थानकों चली गयीं। जिस
- **Translation**: 

---

### Verse 19 (Bramha 0.3979)
- **Original**: है। हृव्य, कव्य, अमृत तथा जो कुछ भी भोजनके स्थानपर ओषधियोंने समस्त पाप-संतापका निवारण
- **Translation**: 

---

### Verse 20 (Bramha 0.3980)
- **Original**: काम आता है, बह हमारा ही श्रेष्ठ अंश है--यह
- **Translation**: 

---

