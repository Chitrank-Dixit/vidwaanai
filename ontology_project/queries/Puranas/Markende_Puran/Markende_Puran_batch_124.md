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

### Verse 1 (Markende Puran 0.2461)
- **Original**: 196 सहिषासुरते 'मैंसेका रूप धारण करके देवीके गणोंकों त्रास देना आरम्प किया
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2462)
- **Original**: किन्हींको धूथुनसे मारकर, किन्हींके ऊपर ख़ुरोंका प्रहार करके, किन्‍्हीं-किन्हींकों पूँछसे चोट पहुँचाकर, कुछको सोंगोंसे विदीर्ण करके, कुछ गणोंक्रो बेगसे, किन्हौंको सिंहनादसे, कुछकों चक्कर देकर और कितनोंकों नि:श्वास ब्रायुके झाँकेसे धराशायी कर दिया
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2463)
- **Original**: 22 - 23
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2464)
- **Original**: इस प्रकार गणोंको सेनाकों
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2465)
- **Original**: गिराकर वह असुर महादेवोके सिंहकों मारलेके लिये झपटा। इससे जगदम्बाकों बड़ा क्रोध
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2466)
- **Original**: उधर महापराक्रमी महिषासुर भी । क्रोधमें भस्कर धरतीकों खुरोंसे खोदने जगा तथा अपने सोगोंसे ऊँच्रे-कँचे पर्वतोंकरो उठाकर फेंकने और गर्जने लगा
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2467)
- **Original**: उसके जेगसे चक्कर देगेके कारण एश्ली क्षुष्प्र होकर फटने हगी। उसकी पूँछसे टकगकर समुद्र सत्र अगेरसे धस्तीकों डुबोने लगा।
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2468)
- **Original**: हिलते हुए सौंगोंके आज्ातसे विदीर्ण
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2469)
- **Original**: हॉकर बाइलेंके टुक92-8क ड़ हो गये। उसके' + संक्षिप्त पार्केएडेयपुराण * 3 काथ1 71973 73574
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2470)
- **Original**: 4497 #9#:# 4577 #: # #$ 4 # 66 # 6 & & & 5 5:52:52:::77:2:07%5:0:0 ए 4 हक के धासकी प्रचण्ड वाबुके वेंगसे उड़े हुए सैकड़ों पर्मत आकाशसे गिरने लगे
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2471)
- **Original**: इस फ्रकार क्रोधमें भो हुए उस महादैत्यकों अपनी ओर आते देख चण्डिकाने उसक्ला जंध #रनेके लिये महान्‌ क्रोध किया
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2472)
- **Original**: उन्होंने पाश फेंककर उस पहान्‌ अस॒ुरकों बाँध लिया। उस महाऊंप्राममें लैभ जानेपर उसने भैंसेका रूप त्याग दिया
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2473)
- **Original**: और तत्काल सिंहके रूपमें वह प्रकट हो गया। उस अबस्थामें ज
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2474)
- **Original**: दम्बा ज्यों ही ठसका पस्तक कारटनेको उद्यत हुईं, त्यों ही बह ख़ड़धारी पुरुषके रूपमें दिखायी देने ज्लगा
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2475)
- **Original**: त्तत देवीने तुरंत ही बाणोंकौ वर्धा करके हाल और तलवारके साथ उस पुरुषकों भो बाँध डाला। इतनेमें हो बह महान्‌ गज़राजके रूपमें परिणत हो गया
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2476)
- **Original**: तथा अपनी सूँडूसे देवोके विशाल सिंहको खोंचने और गर्जने लगा। खींचते समय देबीने तलवारसे उसकी सूँडू काट डाली
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2477)
- **Original**: तब उद्र पह्ादैत्यने पुनः भैंसेका शरीर धारण कर लिया और पहलेको ही भाँति चराचर परणियॉसहित
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2478)
- **Original**: +* सेनापतिघोंसहित महिषासुरका 43554.64::29 ह0500 »+& 4 & 6/843 2:20:0% 02177 7 तोनों लोकोंको व्याकुल करने लगा
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2479)
- **Original**: व्ब क्रोधपें भरी हुईं जगन्माता चण्डिका बारँयार उत्तम प्रधुक्ता पात करने और लाल आँखें करके हँसने लगीं
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2480)
- **Original**: उधर बह अल और पराक्रमक्रे मदसे उन्मत्त हुआ राक्षस अपने सींगोंसे चण्डीके ऊपर पर्वतोंको फेंकने लगा और डकारो लगा
- **Translation**: 

---

