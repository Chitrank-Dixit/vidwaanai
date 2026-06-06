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

### Verse 1 (Vaivtpuran 675.5666)
- **Original**: हैं। श्रीकृष्ण-मन्त्रोंका उपासक ही जीवन्मुक्त माना रमणीय गोलोकमें पुण्यमय वृन्दाबनके भीतर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 675.5667)
- **Original**: गया है। जप, तप, तीर्थ और पूजाके बिना केवल रासमण्डलमें परमात्मा श्रीकृष्णकी प्राणाधिका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 675.5668)
- **Original**: मन्त्रग्रहणमात्रसे नर नारायण हो जाता है। राधा मैं ही हूँ। मैं ही दुर्गा, विष्णुमाया तथा
- **Translation**: 

---

### Verse 4 (Vaivtpuran 675.5669)
- **Original**: श्रीकृष्ण-भक्त अपने नाना और उनके ऊपरकी बुद्धिकी अधिष्ठात्री देवी हूँ। वैकुण्ठमें मैं ही सौ पीढ़ियोंका तथा पितासे लेकर ऊपरकी एक लक्ष्मी और साक्षात्‌ सरस्वती देवी हूँ। ब्रह्मलोकमें
- **Translation**: 

---

### Verse 5 (Vaivtpuran 675.5670)
- **Original**: सहस््न पीढ़ियोंका उद्धार करके गोलोकमें जाता मुझे ही ब्रह्माणी तथा वेदमाता सावित्री कहते
- **Translation**: 

---

### Verse 6 (Vaivtpuran 675.5671)
- **Original**: है। नरेश्वर! यह सारभूत ज्ञान मैंने तुम्हें बताया हैं। मैं ही गड़्ा, तुलसी तथा सबकी आधारभूता
- **Translation**: 

---

### Verse 7 (Vaivtpuran 675.5672)
- **Original**: है। सावर्णिक मन्वन्तरके अन्तमें जब तुम्हारे सारे वसुन्धरा हूँ। नरेश्वर! मैंने अपनी कलासे नाना दोष समाप्त हो जायँगे, उस समय मैं तुम्हें प्रकारके रूप धारण किये हैं। मायाद्वारा सम्पूर्ण
- **Translation**: 

---

### Verse 8 (Vaivtpuran 675.5673)
- **Original**: श्रीहरिकी भक्ति प्रदान करूँगी। स्त्रियोंके रूपमें मेरा ही प्रादुर्भाव हुआ है। परम
- **Translation**: 

---

### Verse 9 (Vaivtpuran 675.5674)
- **Original**: कमाँका फल भोगे बिना उनका सैकड़ों पुरुष परमात्मा श्रीकृष्णने अपनी भ्रूभड्रलीलासे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 675.5675)
- **Original**: करोड़ कल्पोंमें भी क्षय नहीं होता है। अपने मेरी सृष्टि की है। उन्हीं पुरुषोत्तमने अपनी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 675.5676)
- **Original**: किये हुए शुभ या अशुभ कर्मका फल अवश्य भ्रूभड़लीलासे उस महान्‌ विराट्की भी सृष्टि की
- **Translation**: 

---

### Verse 12 (Vaivtpuran 675.5677)
- **Original**: ही भोगना पड़ता है।* मैं जिसपर अनुग्रह करती है, जिसके रोमकृपोंमें सदैव असंख्य विश्व-
- **Translation**: 

---

### Verse 13 (Vaivtpuran 675.5678)
- **Original**: हूँ, उसे परमात्मा श्रीकृष्णके प्रति निर्मल, निश्वल ब्रह्माण्ड निवास करते हैं। वे सब-के-सब कृत्रिम
- **Translation**: 

---

### Verse 14 (Vaivtpuran 675.5679)
- **Original**: एवं सुदृढ़ भक्ति प्रदान करती हूँ और जिन्हें ठगना हैं, तथापि मायासे सब लोग उन अनित्य लोकोंमें चाहती हूँ; उन्हें प्रातःकालिक स्वप्रके समान भी सदा नित्यबुद्धि करते हैं। सातों द्वीपों और
- **Translation**: 

---

### Verse 15 (Vaivtpuran 675.5680)
- **Original**: मिथ्या एवं भ्रमरूपिणी सम्पत्ति प्रदान करती हूँ। समुद्रोंसे युक्त पृथ्वी, नीचेके सात पाताल और
- **Translation**: 

---

### Verse 16 (Vaivtpuran 675.5681)
- **Original**: बेटा! मैंने तुम्हें यह ज्ञानकी बात बतायी है। ऊपरके सात स्वर्ग--इन सबको मिलाकर एक
- **Translation**: 

---

### Verse 17 (Vaivtpuran 675.5682)
- **Original**: अब तुम सुखपूर्वक जाओ। विश्व-त्रह्माण्ड कहा गया है, जिसकी रचना ऐसा कहकर महादेवी वहीं अन्तर्धान हो ब्रह्माद्वारा हुई है। इस तरहके जो असंख्य ब्रह्माण्ड
- **Translation**: 

---

### Verse 18 (Vaivtpuran 675.5683)
- **Original**: गयीं। राज्यप्राप्तिका वरदान पाकर राजा देवीकों हैं, उन सबमें पृथक्‌-पृथक्‌ ब्रह्मा, विष्णु और
- **Translation**: 

---

### Verse 19 (Vaivtpuran 675.5684)
- **Original**: नमस्कार करके अपने घरकों चले गये। वत्स शिव आदि विद्यमान हैं। उन सबके ईश्वर श्रीकृष्ण
- **Translation**: 

---

### Verse 20 (Vaivtpuran 675.5685)
- **Original**: नारद! इस प्रकार मैंने तुम्हें दुर्गाजीका परम उत्तम हैं। यही परात्पर ज्ञान है। वेदों, त्रतों, तीथों,
- **Translation**: 

---

