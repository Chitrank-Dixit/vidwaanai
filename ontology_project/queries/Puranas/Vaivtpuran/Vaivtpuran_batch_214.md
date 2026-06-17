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

### Verse 1 (Vaivtpuran 13.10422)
- **Original**: मुस्कराती हुई श्रीराधाने आस्वादन किया। साथ राधिकाकों उनके हाथमें सौंप दिया और भक्ति-
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10423)
- **Original**: हो उनके दिये हुए ताम्बूलको भी श्रीहरिके सामने भावसे वे श्रीकृष्णके सामने खड़े हो गये। ही खाया। श्रीकृष्णने प्रसन्नतापूर्वक अपना चबाया इसी बीचमें आनन्दित और पुलकित हुए
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10424)
- **Original**: हुआ पान श्रीराधाको दिया। राधाने बड़ी भक्तिसे देवगण दुन्दुभि, आनक और मुरज आदि बाजे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10425)
- **Original**: उसे खाया और उनके मुखारविन्दमकरन्दका पान बजाने लगे। विवाहमण्डपके पास पारिजातके
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10426)
- **Original**: किया। इसके बाद मधुसूदनने भी श्रीराधासे फूलोंकी वर्षा होने लगी। श्रेष्ठ गन्धवोने गौत गाये
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10427)
- **Original**: उनका चबाया हुआ पान माँगा, परंतु राधाने और झुंड-की-झुंड अप्सराएँ नृत्य करने लगीं।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10428)
- **Original**: नहीं दिया। वे हँसने लगीं और बोलीं--' क्षमा ब्रह्माजीने श्रीहरिकी स्तुति की और मुस्कराते हुए
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10429)
- **Original**: कीजिये।' माधवने राधाके हाथसे रत्नमय दर्पण उनसे कहा-'आप दोनोंके चरणकमलोमें मेरी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10430)
- **Original**: ले लिया और राधिकाने भी माधवके हाथसे भक्ति बढ़े, यही मुझे दक्षिणा दीजिये।' ब्रह्माजीको
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10431)
- **Original**: बलपूर्वक उनकी मुरली छीन ली। राधाने माधवका बात सुनकर स्वयं श्रीहरिने उनसे कहा--ब्रह्मन्‌!
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10432)
- **Original**: और माधवने राधाका मन मोह लिया। प्रेम- मेरे चरणकमलोंमें तुम्हारी सुदृढ़ भक्ति हो। अब
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10433)
- **Original**: मिलनके पश्चात्‌ राधाने प्रसन्नतापूर्वक परमात्मा तुम अपने स्थानको जाओ। तुम्हारा कल्याण
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10434)
- **Original**: श्रीकृष्णकों उनकौ मुरली लौटा दी। श्रीकृष्णने भी होगा, इसमें संशय नहीं है। वत्स! मैंने जो कार्य
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10435)
- **Original**: राधाको उनका दर्पण और उज्ण्घल क्रीड़ा-कमल तुम्हारे जिम्मे लगाया है, उसका मेरी आज्ञाके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10436)
- **Original**: दे दिया। उनके केशोंकी सुन्दर वेणी बाँध दी अनुसार पालन करो। और भालदेशमें सिन्दूरका तिलक लगाया। विचित्र मुने! श्रीकृष्फणा यह आदेश सुनकर जगत्‌-
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10437)
- **Original**: पत्र-रचनासे युक्त सुन्दर बेष सँबारा। उन्होंने जैसी विधाता ब्रह्मा श्रीराधा-कृष्णको प्रणाम करके
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10438)
- **Original**: वेष-रचना को, उसे विश्वकर्मा भी नहीं जानते प्रसन्नतापूर्वक अपने लोकको चले गये। ब्रह्माजीके हैं; फिर सखियोंकी तो बात ही क्‍या है? चले जानेपर मुस्कराती हुई देवी राधिकाने बाँको जब राधा श्रीकृष्णकी वेष-रचना करनेको चितवनसे श्रीहरिके मुँहह्ी ओर देखा और
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10439)
- **Original**: उच्यत हुईं, तब वे किशोरावस्थाका रूप त्यागकर लज्जासे अपना मुँह दँक लिया। उस समय उनका
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10440)
- **Original**: पुनः शिशुरूप हो गये। राधाने देखा, बालरूप
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10441)
- **Original**: 468 + संक्षिप्त ब्रह्मवैवर्तपुराण के %$%$%%##%#######%####### # ### ### #;ऋ# ##% # # # # % # % %%%###%% %%क#% #% क्क्कफऋऋ्ऋऋऋऋ कक फ 4 44 ######ऋ#% श्रीकृष्ण क्षुधासे पीड़ित हो रहे हैं। नन्दने जैसे
- **Translation**: 

---

