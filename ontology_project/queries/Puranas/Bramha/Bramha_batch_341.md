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

### Verse 1 (Bramha 0.6801)
- **Original**: अपने कुलका भी संहार कर डाला। अन्तमें और भी सुन्दर स्त्रियाँ थीं। बलभद्रजी रमणियोंके
- **Translation**: 

---

### Verse 2 (Bramha 0.6802)
- **Original**: स्वयम्भू श्रीकृष्ण ट्वारकापुरी छोड़कर अपने अंशभूत बोचमें विराजमान थे और वे उनके सुयशका गान
- **Translation**: 

---

### Verse 3 (Bramha 0.6803)
- **Original**: बलराम आदिके साथ पुन; अपने आश्रयभूत परम कर रही थीं। इसी समय द्विविद भी वहाँ आया
- **Translation**: 

---

### Verse 4 (Bramha 0.6804)
- **Original**: धामको चले गये। और उनके सम्मुख खड़ा हो उन्हींकी नकल।
- **Translation**: 

---

### Verse 5 (Bramha 0.6805)
- **Original**: मुनियोंने पूछा--ब्रह्मन्‌! भगवानने ब्राह्मणोंके करने लगा। वह दुष्ट बानर उन युवतियोंकी ओर
- **Translation**: 

---

### Verse 6 (Bramha 0.6806)
- **Original**: शापको निमित्त बनाकर किस प्रकार अपने कुलका देख-देखकर जोर-जोरसे हँसने लगा। यह देखकर
- **Translation**: 

---

### Verse 7 (Bramha 0.6807)
- **Original**: संहार किया? बलभद्रजीने कुपित होकर उसे डाँटा, किंतु उनके
- **Translation**: 

---

### Verse 8 (Bramha 0.6808)
- **Original**: व्यासजी बोले--एक समयकी बात है-- डाँटनेकी परवा न करके वह किलकारी मारने
- **Translation**: 

---

### Verse 9 (Bramha 0.6809)
- **Original**: पिण्डारक नामके महातीर्थमें विश्वामित्र, कण्व लगा। तब बलरामजीने उठकर बड़े रोषके साथ
- **Translation**: 

---

### Verse 10 (Bramha 0.6810)
- **Original**: तथा महामुनि नारद पधारे थे। वहाँ यदुकुलके मूसल हाथमें लिया। उधर बानरने भी एक कुमारोंने उनका दर्शन किया। वे सभी कुमार भयंकर शिलाखण्ड उठा लिया और उसे बलभद्रजीपर
- **Translation**: 

---

### Verse 11 (Bramha 0.6811)
- **Original**: यौवनके मदसे उन्मत्त थे, अत: भावीकी प्रेरणासे चलाया; किंतु उन्होंने मूसलसे मारकर उस ' उन्होंने जाम्बबतीकुमार साम्बकों स्त्रीके वेषमें शिलाके सहस्रों टुकड़े कर दिये। द्विविदने बलरामजीके
- **Translation**: 

---

### Verse 12 (Bramha 0.6812)
- **Original**: विभूषित किया और मुनियोंको प्रणाम करके मूसलका वार बचाकर उनको छातौमें बड़े वेग
- **Translation**: 

---

### Verse 13 (Bramha 0.6813)
- **Original**: विनीत भावसे पूछा--' महर्षियो ! यह स्त्री पुत्रकी और रोषके साथ घूसा मारा। यह देख बलरामजीने
- **Translation**: 

---

### Verse 14 (Bramha 0.6814)
- **Original**: अभिलाषा रखतो है। बताइये, यह अपने पेटसे भी क्रोधमें भरकर मुक्केसे उसके मस्तकपर प्रहार
- **Translation**: 

---

### Verse 15 (Bramha 0.6815)
- **Original**: कया जनेगी?' वे महर्थि दिव्य ज्ञानसे सम्पन्न थे, किया। इससे वह रक्त वमन करता हुआ निर्जीब 27% 80 22: 4003. 32 होकर पृथ्वीपर गिर पड़ा। गिरते समय उसके के 8 शरीरके आघातसे उस पर्वत-शिखरके सैकड़ों टुकड़े हो गये, मानो उसपर वज्र गिरा हो। उस । समय देवता बलरामजीके ऊपर फूलोंकी वर्षा तथा उनकी भूरि-भूरि प्रशंसा करने लगे और । रे बोले-“वीर! आपने यह बड़ा अच्छा कार्य
- **Translation**: 

---

### Verse 16 (Bramha 0.6816)
- **Original**: ्डेः किया, यह दुष्ट बानर दैत्य-पक्षका सहायक था। । इसने सम्पूर्ण जगत॒कों संकटमें डाल रखा था।, इस प्रकार इस पृथ्वोंको धारण करनेवाले, परम बुद्धिमान्‌ बलशामजीके अनेक अद्भुत पराक्रम
- **Translation**: 

---

### Verse 17 (Bramha 0.6817)
- **Original**: हैं, जिनकी कोई गणना नहों हो सकती।
- **Translation**: 

---

### Verse 18 (Bramha 0.6818)
- **Original**: इस तरह इस जगत्‌का उपकार करनेके लिये
- **Translation**: 

---

### Verse 19 (Bramha 0.6819)
- **Original**: बलरामसहित भगवान्‌ श्रीकृष्णने दैत्यों और दुष्ट राजाओंका वध किया। फिर अर्जुनके साथ
- **Translation**: 

---

### Verse 20 (Bramha 0.6820)
- **Original**: 023 8... न न्य मिलकर भगवामूने अनेक अक्षौहिणी सेनाओंका
- **Translation**: 

---

