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

### Verse 1 (Vishnu Puran 0.2401)
- **Original**: डड पुरोहिता ऊचुः अीविय्णुपुराण [ अ« 19 दुःसह दुःखसे रक्षा करो
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2402)
- **Original**: “सर्वव्यापी जगदुरु भगवान्‌ किष्णु सभी प्राणियोंमें व्याप्त हैं --इस सत्पके प्रभावसे ये पुरोहितगण जीनित हो जायें
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2403)
- **Original**: यदि मैं सर्वष्यापी और अक्षय श्रीविष्णुधगवान्‌को अपने बिपक्षियोंमें भी देखता हूँ तो ये प्रोहितमण जीबित हो जायै
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2404)
- **Original**: जो लोग मुझे मारनेके लिये आये, जिन्होंने मुझे विष दिया, जिन्होंने आगमें जल्त्या, जिन्होंने दिग्गजोंसे पीडित कराया और जिन्होंने सपोंसे डैंसाया उन सबके प्रति यदि मैं समान मित्रभावसे रहा हूँ और मेरी कभी पाप - बुद्धि नहीं हुई तो उस सत्यके प्रभावसे ये दैत्यपुरोहित जी उठे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2405)
- **Original**: श्रीपराशरजी खोले--ऐसा कहकर उनके स्पर्दा करते हो ये ब्राह्मण स्वस्थ होकर ठठ बैठे और उस विनयावनत बालकसे कहने लगे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2406)
- **Original**: पुरोश्चितगण बोर्ै--हे वत्स ! तू बड़ा श्रेष्ठ है। तू दीर्षायु, निईन्द्र, बल-बीर्यसम्पन्न तथा पुत्र, पौत्र एवं धन-ऐश्वर्यादिसे सम्पन्न हो
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2407)
- **Original**: औपराज्षर उवाच श्रीपराहरजी खोले--हे महामुने ! ऐसा कह इत्युक्त्वा त॑ ततो गत्वा यथावृत्तं पुरोहिता:। ..
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2408)
- **Original**: पुरोहितोने दैत्यराज हिरण्यकशिपुके पास जा उसे सारा दैत्ववाजाय. सकस्ठमाचचस्युर्महामुने
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2409)
- **Original**: समाचार ज्यों-का-त्यों सुना दिया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2410)
- **Original**: «0.0 और “-+++ इति श्रीविष्णुपुराणे प्रथमेंडशे अष्टादशो5ध्याय:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2411)
- **Original**: च्तत्ल और “++- उन्नीसवाँ अध्याय त्रह्मादकृत भगवत्‌-गुण-वर्णन और भ्रह्लादकी रक्षाके लिये भगवानका सुदर्शनचक्रको भेजना औपरादार उवाच अपराशरजी जोले--हिरण्यकाश्रिपुने कृत्याको हिरण्यकशिपु: श्रुत्वा ता कृत्यां बितथीकृताम्‌ । भी विफल हुई सुन अपने पुत्र प्रह्भादकों बुक्लाकर उनके इस आहृय पुत्र॑ पप्नच्छ प्रभावस्थास्य कारणम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2412)
- **Original**: प्रभावका कारण पूछा
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2413)
- **Original**: हिरण्यकशिपुस्वाच हिरण्यकक्षिपु खोल्छा--ओरे प्रह्मद ! तू बड़ा 80% क:40>:0की- सु है यह ! 2
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2414)
- **Original**: मभावशाली है! तेरी ये चेषटएँ मन््रादिजनित है या 1255 कै स्वाभाविक ही हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2415)
- **Original**: एवं पृष्टस्तदा पित्ना प्रह्मादोडसुरबालक: । श्रीपराशरजी खोले--पिताके इस प्रकार पूछनेपर अणिपत्व पितुः पादाविद॑ वच्ननमब्रचीत्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2416)
- **Original**: दैत्वकुमार प्रह्मादजीने उसके चरणोंमें प्रणाम कर इस
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2417)
- **Original**: अं 19 ] न मन्त्रादिकृत तात न च नैसर्गिको मम । प्रभाव एव सामान्यो यस्य यस्थाच्युतो हंदि।। 4 अन्येषां यो न पापानि चिन्तयत्यात्मनो यथा । तस्य पापागमस्तात हेत्वभावान्न विद्यते। 5 कर्मणा घनसा वाचा परपीडां करोति यः । तद्दीज जन्म फलति प्रभूत तस्य चाझुभम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2418)
- **Original**: 6 सो5हं न पापमिच्छामि न करोमि वदामि वा । क्िन्तयन्सर्वभूतस्थमात्मन्यप चर केशवम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2419)
- **Original**: 7 पक जनता के मे नया मानस दुःखं देव भूतभव्र तथा। तस्य में जायते कुत:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2420)
- **Original**: 8 एवं सर्वेषु भूतेषु भक्तिरव्यभिचारिणी । कर्तव्या पण्डितैज्ञात्वा सर्वभूतमर्य हरिम
- **Translation**: 

---

