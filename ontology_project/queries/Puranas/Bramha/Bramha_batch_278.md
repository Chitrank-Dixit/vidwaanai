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

### Verse 1 (Bramha 0.5541)
- **Original**: हँसकर पूछा-“सब धर्मोंके ज्ञाता महात्माजी! हुई। कण्डुमुनि स्नान, संध्या, जप, होम, स्वाध्याय,
- **Translation**: 

---

### Verse 2 (Bramha 0.5542)
- **Original**: क्या आज ही आपका दिन बीता है? आपकी यह देवपूजन, व्रत, उपवास, नियम और ध्यान-सब । बात ! छोड़कर रात-दिन उसीके साथ विहार करने लगे। इसीमें वे आनन्द मानते थे। उनका हृदय कामदेवके वशीभूत हो गया था। अतः वे अपनी तपस्याकी हानि नहीं समझ पाते थे। इस प्रकार कण्डुमुनि
- **Translation**: 

---

### Verse 3 (Bramha 0.5543)
- **Original**: उसके साथ सांसारिक विषयभोगमें आसक्त हो
- **Translation**: 

---

### Verse 4 (Bramha 0.5544)
- **Original**: 5 सौसे कुछ अधिक वर्षोतक मन्दराचलकी गुफामें
- **Translation**: 

---

### Verse 5 (Bramha 0.5545)
- **Original**: परेजी। जा किप्रओनत नहांगत अनादुत
- **Translation**: 

---

### Verse 6 (Bramha 0.5546)
- **Original**: कहा--“ब्रह्मन्‌! अब मैं स्वर्गमें जाना चाहती हूँ। आप प्रसन्न होकर मुझे जानेकी आज्ञा दें।' मुनिका मन तो उसीमें आसक्त हो रहा था। ठसके इस प्रकार पूछनेपर वे बोले--'कल्याणी! कुछ दिन
- **Translation**: 

---

### Verse 7 (Bramha 0.5547)
- **Original**: और ठहरो।' तब उसने पुनः सौ वर्षोंसे कुछ अधिक कालतक उन कण्डुमुनिके -साथ विषय
- **Translation**: 

---

### Verse 8 (Bramha 0.5548)
- **Original**: प्र कं भोगा। तदनन्तर उसने पुनः जानेकी आज्ञा माँगी, 2337 मने... किंतु मुनिने स्वीकार नहीं किया। अत: उसे
- **Translation**: 

---

### Verse 9 (Bramha 0.5549)
- **Original**: मुनि बोले--कल्याणी! अभी प्रात:काल ही लगभग दो सौ वर्षोताक और ठहरना पड़ा। वह
- **Translation**: 

---

### Verse 10 (Bramha 0.5550)
- **Original**: तो तुम इस नदीके सुन्दर तटपर आयी हो। उसो जब-जब उनसे देवलोकमें जानेकी आज्ञा माँगती,
- **Translation**: 

---

### Verse 11 (Bramha 0.5551)
- **Original**: समय मैंने तुम्हें देखा, परिचय पूछा और तुम मेरे तब-तब वे उसे यही उत्तर देते-कुछ दिन और
- **Translation**: 

---

### Verse 12 (Bramha 0.5552)
- **Original**: साथ आश्रममें आयी। अब वह दिन बीता है और ठहरो। प्रम्लोचा एक तो मुनिके शापसे डरती थी।
- **Translation**: 

---

### Verse 13 (Bramha 0.5553)
- **Original**: यह संध्याका समय उपस्थित हुआ है। फिर यह दूसरे उसमें दक्षिणा नायिकाकों स्वाभाविक उदारता
- **Translation**: 

---

### Verse 14 (Bramha 0.5554)
- **Original**: परिहास किसलिये? सच्ची बात बताओ। थी और तीसरे वह प्रणयभज्भकी पीड़ाको जानती
- **Translation**: 

---

### Verse 15 (Bramha 0.5555)
- **Original**: . प्रम्लोचाने कहा--ब्रह्मनू ! यह ठीक है कि थी। इसलिये मुनिको छोड़ न सकी। महर्षि ' मैं प्रातःकालमें ही आयो थी; इसमें तनिक भी 9450
- **Translation**: 

---

### Verse 16 (Bramha 0.5556)
- **Original**: रु हद (858
- **Translation**: 

---

### Verse 17 (Bramha 0.5557)
- **Original**: 268 + संक्षिप्त ब्रह्मपुराण « कक 3 जनलकककभम "3 क्‍पध्ध धरना न शक कं 7 :-धथककट--चचचतच"च््ं्ँ्?्ल्िेिखल्ललल खा ्ववयशरशशगकलललल स्च्चचचि मिथ्या नहीं है। किंतु आज तबसे सैकड़ों वर्ष
- **Translation**: 

---

### Verse 18 (Bramha 0.5558)
- **Original**: तुझे अपने क्रोधकी प्रचण्ड आगसे जो भस्म नहीं बीत गये।
- **Translation**: 

---

### Verse 19 (Bramha 0.5559)
- **Original**: करता, इसमें एक कारण है--सत्पुरुषोंकी मैत्री यह सुनकर मुनिकों बड़ा भय हुआ। उन्होंने
- **Translation**: 

---

### Verse 20 (Bramha 0.5560)
- **Original**: सात पग एक साथ चलनेसे ही हो जाती है। मैं विशाल नेत्रोंवाली अप्सरासे पूछा-' भीरु! बताओ
- **Translation**: 

---

