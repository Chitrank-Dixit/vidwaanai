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

### Verse 1 (Narsihma Puran 0.1)
- **Original**: 3» भमो भगवते अ्रीनृसिंहाय नमः प्रयागमें ऋषियोंका समागम। सूतजीके प्रति भरद्वाजजीका प्रइन; सूतजीद्वारा कथारम्भ और सृुप्टिक्रमका वर्णन
- **Translation**: 

---

### Verse 2 (Narsihma Puran 0.2)
- **Original**: आीलक्ष्मीनृसिंहाय नमः
- **Translation**: 

---

### Verse 3 (Narsihma Puran 0.3)
- **Original**: आवेदव्यासाय नपः
- **Translation**: 

---

### Verse 4 (Narsihma Puran 0.4)
- **Original**: नारायणं नमस्कृत्य नर चैव नरोत्तमम्‌। देवीं सरस्वती चैव ततो जयमुदीरयेत्‌
- **Translation**: 

---

### Verse 5 (Narsihma Puran 0.5)
- **Original**: तप्तहाटककेशान्तज्वलत्पावकलोचन
- **Translation**: 

---

### Verse 6 (Narsihma Puran 0.6)
- **Original**: चज़ाधिकनखस्पर्श दिव्यसिंह नमोउस्तु ते
- **Translation**: 

---

### Verse 7 (Narsihma Puran 0.7)
- **Original**: पान्तु वो नरसिंहस्य कस नमक, ;
- **Translation**: 

---

### Verse 8 (Narsihma Puran 0.8)
- **Original**: हिरण्बकशिपोर्वक्ष:क्षेत्रास॒क्‌कर्दपारुणा:
- **Translation**: 

---

### Verse 9 (Narsihma Puran 0.9)
- **Original**: हिमवद्वासिन: सर्वे मुनयो वेदपारगा:। ब्रिकालज्ञा महात्मानो मैमिषारण्यवासिनः
- **Translation**: 

---

### Verse 10 (Narsihma Puran 0.10)
- **Original**: ये5र्बुंदारण्यनिरता:. पुष्करारण्ययासिन:। महेन्रादिरता ये च ये च विन्ध्यनिवासिन:
- **Translation**: 

---

### Verse 11 (Narsihma Puran 0.11)
- **Original**: धर्मारण्यरता ये च॑ दण्डकारण्यवासिन:। श्रीशैलनिरता ये चर कुरुक्षेत्रनिवासिन:
- **Translation**: 

---

### Verse 12 (Narsihma Puran 0.12)
- **Original**: कौमारपर्वते ये चर ये च्र॒ पम्पानिवासिन:। एते चान्ये च बहव: सशिष्या मुनयो5मला:
- **Translation**: 

---

### Verse 13 (Narsihma Puran 0.13)
- **Original**: माघमासे प्रयागं तु स्तातुं तीर्थ समागता:। तत्र स््ात्वा यथान्याय॑ कृत्वा कर्म जपादिकम्‌
- **Translation**: 

---

### Verse 14 (Narsihma Puran 0.14)
- **Original**: डे 8 अन्तयाँमी भगवान्‌ नारायण (श्रोकृष्ण) उतके सखा नरत्रेष्ट नर (अर्जुन) तथा इनको लीला प्रकट करनेवालो सरस्वती देवोको नमस्कार करनेके पश्चात्‌ ' जय' (इतिहास पुराण)-का पाठ करे
- **Translation**: 

---

### Verse 15 (Narsihma Puran 0.15)
- **Original**: दिव्य सिंह! तपाये हुए सुवर्णके समान पीले केशोकि भीतर प्रज्वलित अप्रिफी भाँति आपके नेत्र देदौप्यमान हो रहे हैं तथा आपके न्खोंका स्पर्श बज़्से भी अधिक कठोर है, इस प्रकार अमित प्रभावशाली आप परमेश्वरको मेरा नमस्कार है। भगवान्‌ नृसिह्के नखरूपी हलके अग्रभाग, जो हिरण्यकशिपु नामक दैत्यके वक्ष:स्थलरूपी खेतकी रक्तमयी कीचड़के लगनेसे लाल हो गये हैं, आप लोगोंकी रक्षा करें
- **Translation**: 

---

### Verse 16 (Narsihma Puran 0.16)
- **Original**: एक समय हिमालयकी घाटियोंमें रहनेब्राले, ग्रेदोंके पारगामी एवं प्रिकालवेत्ता समस्त महात्मा समुनिगण नैमिषारण्य, अर्चुदारण्य और पुष्करारण्यके नियासो मुनि, महेन्द्र पर्वत और विन्ध्यगिरिके निवासी ऋषि, धर्मारण्य, दण्डकारण्य, श्रोशैल और कुरुक्षेत्रमें वास करनेवाले मुनि तथा कुमार पर्वत एवं पम्मासरके निवासी ऋषि-ये तथा अन्य भी यहुत-से शुद्ध ददयबाले महपिंगण अपने शिष्योंके साथ माघके महीनेमें स्ताव करतेके लिये प्रयाग-तीर्थमें आवे # 4ड--3/, # जहाँपर यथोचित रीतिसे स्तान और जप आदि करके
- **Translation**: 

---

### Verse 17 (Narsihma Puran 0.17)
- **Original**: 3 श्रीनरसिंहपुराण नत्वा तु माधव देवं कृत्वा च पितृतर्पणम्‌। वृष्ठा तत्र भरद्वाजं पुण्बतीर्थनिवासिनपू
- **Translation**: 

---

### Verse 18 (Narsihma Puran 0.18)
- **Original**: 9 ते पूजयित्वा विधिवत्तेनेव चर सुपूजिता:। आसनेषु विचित्रेषु यृष्यादिषु यथाक्रमम्‌
- **Translation**: 

---

### Verse 19 (Narsihma Puran 0.19)
- **Original**: 10 भरद्वाजेन दत्तेषु आसीनास्ते तपोधना:। कृष्णाश्रिता: कथा: सर्वे परस्परमथाबुबन्‌
- **Translation**: 

---

### Verse 20 (Narsihma Puran 0.20)
- **Original**: 11 कथान्तेषु ततस्तेषां मुनीनां भावितात्मनाम्‌। आजगाम महातेजास्तत्र सूतों महामति:
- **Translation**: 

---

