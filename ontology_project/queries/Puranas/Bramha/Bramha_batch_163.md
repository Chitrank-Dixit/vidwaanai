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

### Verse 1 (Bramha 0.3241)
- **Original**: अकथनीय है।* कहकर दुःखो हुए राजा भौवन अपने पुरोहित। तुमने जो प्रचुर दक्षिणासे युक्त यह अश्वमेध- कश्यपके साथ यृहस्पतिजीके ज्येष्ठ भ्राता संवर्तके
- **Translation**: 

---

### Verse 2 (Bramha 0.3242)
- **Original**: यड्ध किया है, इससे तुम कृतार्थ हो गये। अब इस पास गये और इस प्रकार बोले--' भगवन्‌! मुझे
- **Translation**: 

---

### Verse 3 (Bramha 0.3243)
- **Original**: विषयमें तुम्हें अन्यथा विचार नहीं करना चाहिये। ऐसा कोई उत्तम प्रदेश बतलाइये, जहाँ एक ही
- **Translation**: 

---

### Verse 4 (Bramha 0.3244)
- **Original**: तिल, गौ, धन, धान्य-जो कुछ भी गोदाबरोके साथ आरम्भ किये हुए दस अश्वमेध-यज्ञ पूर्ण हो
- **Translation**: 

---

### Verse 5 (Bramha 0.3245)
- **Original**: तटपर दिया जाता है, वह सब अक्षय हो जाता है। जायें।' तब मुनिश्रेष्ठ संबर्तने कुछ कालतक ध्यान
- **Translation**: 

---

### Verse 6 (Bramha 0.3246)
- **Original**: यह सुनकर सप्राट्‌ भौवनने ब्राह्मणोंको बहुत- करके महाराज भौवनसे कहा-' ब्रह्माजीके पास
- **Translation**: 

---

### Verse 7 (Bramha 0.3247)
- **Original**: सा अन्नदान किया। तबसे वह तीर्थ दशाश्वमेधिकके जाओ। वे ही उत्तम प्रदेश बतायेंगे। नामसे विख्यात हुआ। वहाँ स्नान करनेसे दस महाबुद्धिमान्‌ भौवन महात्मा कश्यपकों साथ
- **Translation**: 

---

### Verse 8 (Bramha 0.3248)
- **Original**: अश्वमेध-यज्ञोंका फल प्राप्त होता है। भूमिदानस्पूहां त्यकत्ता अन्न॑ देहि महाफलम्‌। नान्नदाउसमं पुर्ण्य त्िपु. लोकेषु . विद्यते
- **Translation**: 

---

### Verse 9 (Bramha 0.3249)
- **Original**: विशेषतस्तु गद्गाया: श्रद्धया पुलिने मुने
- **Translation**: 

---

### Verse 10 (Bramha 0.3250)
- **Original**: 21-22)
- **Translation**: 

---

### Verse 11 (Bramha 0.3251)
- **Original**: 156 * संक्षिप्त ब्रह्मपुराण « उससे आगे पैशाचतीर्थ है, जो ब्रह्मबादी
- **Translation**: 

---

### Verse 12 (Bramha 0.3252)
- **Original**: और अद्विकाके गर्भसे निर्क्तिके अंशसे पिशाचोंका महर्षियोंद्वारा सम्मानित है। यह गोदावरीके दक्षिण- , राजा अद्ठि उत्पन्न हुआ। इसके बाद उन दोनों तटपर स्थित है। अब मैं उसका स्वरूप बतलाता
- **Translation**: 

---

### Verse 13 (Bramha 0.3253)
- **Original**: स्थत्रियोंने उक्त देबताओंसे कहा--'हमें मुनिके हूँ, सुनो। मुनिश्रेष्ठ नारद! ब्रह्मगिरिके पार्श्रभागमें
- **Translation**: 

---

### Verse 14 (Bramha 0.3254)
- **Original**: बरदानसे पुत्र तो प्राप्त हुए, किंतु इन्द्रके शापसे अञ्न नामसे प्रसिद्ध एक पर्वत है। वहाँ एक
- **Translation**: 

---

### Verse 15 (Bramha 0.3255)
- **Original**: हमारा मुख कुरूप होनेके कारण सारा शरौर ही सुन्दरी अप्सरा शापभ्रष्ट होकर उत्पन्त हुई। उसका
- **Translation**: 

---

### Verse 16 (Bramha 0.3256)
- **Original**: विकृत हो गया है। इसे दूर करनेके लिये हम क्या नाम अझ्जना था। उसके सब अड्ग बहुत सुन्दर थे,
- **Translation**: 

---

### Verse 17 (Bramha 0.3257)
- **Original**: उपाय करें-इसे आप दोनों बतायें।' तब भगवान्‌ किंतु मुँह वानरीका था। केसरी नामक श्रेष्ठ वानर , वायु और निर्क्तिने कहा--'गोदाबरीमें स्नान और अज्ञनाके पति थे। केसरीके एक दूसरी भी स्त्री
- **Translation**: 

---

### Verse 18 (Bramha 0.3258)
- **Original**: दान करनेसे तुम्हें शापसे छुटकारा मिल जायगा।' थी, जिसका नाम अद्विका था। वह भी शापश्रष्ट
- **Translation**: 

---

### Verse 19 (Bramha 0.3259)
- **Original**: यों कहकर वे दोनों वहीं अन्तर्धान हो गये। तब अप्सरा ही थी। उसके भी सब अक्ञ सुन्दर थे।
- **Translation**: 

---

### Verse 20 (Bramha 0.3260)
- **Original**: पिशाचरूपधारो अद्विने अपने भाई हनुमानूजीको किंतु मुँह बिल्लीके समान था। अद्विका भी अज्जन
- **Translation**: 

---

