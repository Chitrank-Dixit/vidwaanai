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

### Verse 1 (Vishnu Puran 0.2461)
- **Original**: उस हीघ्रगामो सुदर्शनचक्तो उस यालककी रक्षा करते हुए शम्बरासुरकी सहस्त्रों मायाओको एक-एक करके नष्ट कर दिया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2462)
- **Original**: तब दैत्यगाजने सबको सुखा डालनेवाले वायुसे कहा कि मेरी आज्ञासे तुम शीघ्र ही इस दुरात्पाको नष्ट कर दो
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2463)
- **Original**: अतः उस अति तीज शीवल्त और रूक्ष बायुने, जो अति असहनीय था 'जो आज्ञा" कह उनके शरोरको सुखानेके लिये उसमें प्रवेश किया
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2464)
- **Original**: अपने शरीरमें वायुका आबेश हुआ जान दैत्यकुमार प्रह्मादने भगवान्‌ चरणीघरको इृटयमें धारण किया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2465)
- **Original**: उनके हदयमें स्थित हुए श्रीजनार्दनने क्रुद् होकर उस भोषण वायुकत पी लिया, इससे वह क्षीण हो गया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2466)
- **Original**: इस प्रकार पवन और सम्पूर्ण मायाओंके क्षीण हो जानेपर महामति प्रह्लादज़ी अपने गुरुके घर चले गये
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2467)
- **Original**: तदनत्तर गुरजी उन्हें नित्यप्रति शुक्ताचार्यजीकी बनायी हूई राज्यफलप्रदायिनी राजनीतिका अध्ययन कराने लगे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2468)
- **Original**: जन गुर्जीने उन्हें नीतिझ्ाख्ममें निपुण और विनयसम्पन्न देखा तो उनके पितासे कहा-- अब यह स॒तिक्षित हो गया है'
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2469)
- **Original**: आचार्य बोले--हे दैत्यगाज ! अब हमने तुम्झरे पुत्रको नीतिशास्त्रमें पूर्णतया निषुण कर दिया है, भृगु- ऋचदन चुक़ाचार्यजीने जो कुछ कहा है उसे प्रक्लाद तत्त्वतः जानता है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2470)
- **Original**: हिरण्यकक्षिपु बोला--प्रह्लद! [यह तो बता ] राजाक़ों मित्रोंसे कैसा बर्ताव करना चाहिये ? और तञात्रुओंसे कैसा 7 तथा त्रिह्मेकीमें जो मध्यस्थ (दोनों पक्षोके हितचिल्तक) हों, उनसे किस ग्रकार आचरण करे ?
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2471)
- **Original**: मन्तियों, अमात्यों, बाह्य और (जिकें जीतकर बल्मत्‌ दास बना लिया हो) तथा अन्यान्य जनोंके प्रति किस प्रकार व्यवहार करना चाहिये 2?
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2472)
- **Original**: हे प्रह्माद ! यह ठीक-ठीक बता कि करने और न करनेयोग्य कार्योंकाा विधान किस प्रकार करे, दुर्ग और आटविक (जंगल्जी मनुष्य) आदिकों किस प्रकार वज्ञीभूत करे और गुप्त कन्ुरूप क्य्रटेको
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2473)
- **Original**: प्रथम अंश «9 तथा मे कथ्यता ज्ञातुं तवेच्छामि मनोगतम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2474)
- **Original**: 32 श्रोपयाशर उचाच अणिपत्य पितुः पादो तदा प्रश्रयभूषण: । अ्रह्मादः प्राह दैत्येद्ं कृताअल्‍्पुटस्तथा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2475)
- **Original**: 33 प्रह्मद उवाच ममोपदिष्टं सकले गुरुणा नात्र संशय: । गृहीतत्तु मया किन्तु न सदेतन्मते मम
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2476)
- **Original**: 34 साम चोपप्रदानं ् भेददण्डौ तथापरौ। उपाया: कथ्षिता: सर्वे मित्रादीनां च साथने
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2477)
- **Original**: 35 तानेबाहू न पश्यामि मित्रार्दीस्तात मा क़ुध: । साध्याभावे महाबाहो साधने: कि प्रयोजनम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2478)
- **Original**: 36 सर्वभूतात्यके तात जगजन्नाथे जगन्यये। परमात्पनि गोविन्दे मिन्नामिद्रकथा कुतः
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2479)
- **Original**: 37 त्व्यस्ति भगवान्‌ विष्णुर्पयि चान्यत्र चास्ति सः । अतस्ततोउ्य मित्र मे शात्रुश्षति पृथक्कतः
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2480)
- **Original**: 38 +0 27% टंडन ही
- **Translation**: 

---

